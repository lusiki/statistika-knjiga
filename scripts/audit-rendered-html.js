/* Manual browser audit for the complete rendered HTML book.
 *
 * Usage (PowerShell):
 *   $env:NODE_PATH = "<directory containing playwright>"
 *   $env:AUDIT_BASE = "http://127.0.0.1:8899"
 *   node scripts/audit-rendered-html.js
 *
 * The script checks every canonical route at seven widths in both themes.
 * Every audited case is retained as a full-page screenshot. Very tall pages
 * are split into numbered tiles to avoid Chromium's 16,384 px raster limit.
 */

"use strict";

const { chromium } = require("playwright");
const fs = require("fs");
const os = require("os");
const path = require("path");

const base = process.env.AUDIT_BASE || "http://127.0.0.1:8899";
const outDir = process.env.AUDIT_DIR || fs.mkdtempSync(
  path.join(os.tmpdir(), "statistika-postfix-audit-")
);

const routes = [
  ["/", "root"],
  ["/index.html", "index"],
  ["/chapters/00-predgovor.html", "ch00"],
  ...[
    "01-zasto-statistika",
    "02-mjerenje-i-dizajn",
    "03-kako-brojke-zavode",
    "04-sazimanje-podataka",
    "05-vizualizacija",
    "06-povezanost",
    "07-vjerojatnost",
    "08-uzorkovanje",
    "09-procjena",
    "10-logika-testiranja",
    "11-velicina-ucinka-i-snaga",
    "12-kriza-i-obnova",
    "13-kategoricki-podaci",
    "14-dvije-grupe",
    "15-vise-grupa",
    "16-regresija",
    "17-doba-algoritama",
    "18-vase-prvo-istrazivanje",
  ].map((slug, index) => [
    `/chapters/${slug}.html`,
    `ch${String(index + 1).padStart(2, "0")}`,
  ]),
  ["/references.html", "references"],
  ["/dodaci/a-praktikum.html", "app-a"],
  ["/dodaci/b-jamovi.html", "app-b"],
  ["/dodaci/c-katalog-podataka.html", "app-c"],
  ["/dodaci/d-koji-test.html", "app-d"],
  ["/dodaci/e-rjecnik.html", "app-e"],
  ["/dodaci/f-ai-protokol.html", "app-f"],
  ["/interakcije.html", "interakcije"],
  ["/pojmovnik.html", "pojmovnik"],
  ["/podaci.html", "podaci"],
  ["/uci-s-ai.html", "uci-s-ai"],
  ["/predavanja.html", "predavanja"],
  ["/silabus.html", "silabus"],
  ["/raspored.html", "raspored"],
  ["/resursi.html", "resursi"],
  ["/404.html", "404"],
];

const widths = [1440, 1100, 1000, 768, 600, 390, 320];
const themes = ["light", "dark"];
const screenshotWidths = new Set(widths);
const maxScreenshotTileHeight = 8000;
const routePattern = process.env.AUDIT_ROUTE_PATTERN
  ? new RegExp(process.env.AUDIT_ROUTE_PATTERN)
  : null;
const requestedWidths = process.env.AUDIT_WIDTHS
  ? new Set(
    process.env.AUDIT_WIDTHS
      .split(",")
      .map((value) => Number.parseInt(value.trim(), 10))
      .filter(Number.isFinite)
  )
  : null;
const requestedThemes = process.env.AUDIT_THEMES
  ? new Set(process.env.AUDIT_THEMES.split(",").map((value) => value.trim()))
  : null;
const auditedRoutes = routePattern
  ? routes.filter(([route, label]) => routePattern.test(`${route} ${label}`))
  : routes;
const auditedWidths = requestedWidths
  ? widths.filter((width) => requestedWidths.has(width))
  : widths;
const auditedThemes = requestedThemes
  ? themes.filter((theme) => requestedThemes.has(theme))
  : themes;

async function captureAuditScreenshot(page, filePath) {
  const dimensions = await page.evaluate(() => ({
    width: Math.max(
      document.documentElement.clientWidth,
      document.documentElement.scrollWidth
    ),
    height: Math.max(
      document.body.scrollHeight,
      document.documentElement.scrollHeight
    ),
  }));

  if (dimensions.height <= maxScreenshotTileHeight) {
    await page.screenshot({
      path: filePath,
      fullPage: true,
      type: "jpeg",
      quality: 55,
      animations: "disabled",
    });
    return 1;
  }

  const parsed = path.parse(filePath);
  const partCount = Math.ceil(dimensions.height / maxScreenshotTileHeight);
  const originalViewport = page.viewportSize();
  try {
    for (let part = 0; part < partCount; part += 1) {
      const y = part * maxScreenshotTileHeight;
      const height = Math.min(
        maxScreenshotTileHeight,
        dimensions.height - y
      );
      await page.setViewportSize({ width: dimensions.width, height });
      await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
      await page.evaluate(() => new Promise((resolve) => {
        requestAnimationFrame(() => requestAnimationFrame(resolve));
      }));
      await page.screenshot({
        path: path.join(
          parsed.dir,
          `${parsed.name}_part${String(part + 1).padStart(2, "0")}${parsed.ext}`
        ),
        fullPage: false,
        type: "jpeg",
        quality: 55,
        animations: "disabled",
      });
    }
  } finally {
    if (originalViewport) {
      await page.setViewportSize(originalViewport);
    }
    await page.evaluate(() => window.scrollTo(0, 0));
  }
  return partCount;
}

function isNumberedChapter(route) {
  return /^\/chapters\/(0[1-9]|1[0-8])-/.test(route);
}

function needsWidget(route) {
  return /^\/chapters\/(0[1-9]|1[0-7])-/.test(route);
}

function isStandalone(route) {
  return [
    "/",
    "/index.html",
    "/interakcije.html",
    "/pojmovnik.html",
    "/podaci.html",
    "/uci-s-ai.html",
    "/predavanja.html",
    "/silabus.html",
    "/raspored.html",
    "/resursi.html",
    "/404.html",
  ].includes(route);
}

async function collectMetrics(page, route, width, theme) {
  return page.evaluate(({ currentRoute, currentWidth, currentTheme }) => {
    const shown = (element) => {
      if (!element) return false;
      const style = getComputedStyle(element);
      const box = element.getBoundingClientRect();
      return style.display !== "none" &&
        style.visibility !== "hidden" &&
        Number(style.opacity || 1) > 0 &&
        box.width > 0 &&
        box.height > 0;
    };
    const boxOf = (element) => {
      const box = element.getBoundingClientRect();
      return {
        x: box.x,
        y: box.y,
        width: box.width,
        height: box.height,
        right: box.right,
        bottom: box.bottom,
      };
    };
    const all = (selector) => Array.from(document.querySelectorAll(selector));
    const text = document.body.innerText || "";
    const callouts = all(".callout-vinjeta, .callout-divljina").map((element) => ({
      kind: element.classList.contains("callout-vinjeta")
        ? "vinjeta"
        : "divljina",
      box: boxOf(element),
      scrollWidth: element.scrollWidth,
      clientWidth: element.clientWidth,
      background: getComputedStyle(element).backgroundColor,
      firstTextX: element.querySelector("p")
        ? element.querySelector("p").getBoundingClientRect().x
        : null,
    }));
    const tables = all("table").filter(shown).map((element) => {
      const box = boxOf(element);
      const scroller = element.closest(".table-scrollable");
      const parent = element.parentElement;
      const availableWidth = scroller
        ? scroller.clientWidth
        : (parent ? parent.clientWidth : currentWidth);
      const hint = scroller &&
        scroller.nextElementSibling &&
        scroller.nextElementSibling.classList.contains("table-scroll-hint")
        ? scroller.nextElementSibling
        : null;
      const firstCell = element.querySelector("th:first-child, td:first-child");
      return {
        box,
        scrollWidth: element.scrollWidth,
        clientWidth: element.clientWidth,
        availableWidth,
        needsScroll:
          element.scrollWidth > availableWidth + 1 ||
          box.width > availableWidth + 1,
        parentOverflowX: parent ? getComputedStyle(parent).overflowX : "",
        hasScroller: Boolean(scroller),
        scrollerFocusable: Boolean(scroller && scroller.tabIndex >= 0),
        scrollerLabelled: Boolean(
          scroller && (
            scroller.getAttribute("aria-label") ||
            scroller.getAttribute("aria-labelledby")
          )
        ),
        hintVisible: Boolean(hint && shown(hint)),
        firstColumnSticky: Boolean(
          firstCell && getComputedStyle(firstCell).position === "sticky"
        ),
      };
    });
    const images = all("img").filter(shown);
    const widgetSvgs = all(".widget-frame svg").filter(shown);
    const widgetSvgMetrics = widgetSvgs.map((element) => {
      const box = boxOf(element);
      const viewBox = element.viewBox && element.viewBox.baseVal;
      const intrinsicWidth =
        Number.parseFloat(element.getAttribute("width")) ||
        (viewBox && viewBox.width) ||
        box.width;
      const scale = intrinsicWidth > 0 ? box.width / intrinsicWidth : 1;
      const textSizes = Array.from(element.querySelectorAll("text"))
        .filter(shown)
        .map((textElement) =>
          Number.parseFloat(getComputedStyle(textElement).fontSize) * scale
        )
        .filter(Number.isFinite);
      return {
        width: box.width,
        intrinsicWidth,
        scale,
        minEffectiveText:
          textSizes.length > 0 ? Math.min(...textSizes) : null,
      };
    });
    const h1s = all("main h1, #quarto-content h1").filter(shown);
    const header = document.querySelector("#quarto-header");
    const sidebar = document.querySelector("#quarto-sidebar");
    const pager = document.querySelector(".page-navigation");
    const navbarUtilityMetric = (selector) => {
      const icon = document.querySelector(selector);
      if (!icon) return null;
      const style = getComputedStyle(icon, "::before");
      return {
        visible: shown(icon),
        color: style.color,
        opacity: Number(style.opacity || 1),
        backgroundColor: style.backgroundColor,
        backgroundImage: style.backgroundImage,
        maskImage: style.maskImage || style.webkitMaskImage || "none",
      };
    };
    const navbarUtilityIcons = {
      theme: navbarUtilityMetric(".quarto-color-scheme-toggle .bi"),
      reader: navbarUtilityMetric(".quarto-reader-toggle .bi"),
    };
    const uiAttributeText = all("[aria-label], [title], [placeholder]")
      .map((element) => [
        element.getAttribute("aria-label") || "",
        element.getAttribute("title") || "",
        element.getAttribute("placeholder") || "",
      ].join(" "))
      .join(" ");

    return {
      route: currentRoute,
      width: currentWidth,
      theme: currentTheme,
      docWidth: document.documentElement.scrollWidth,
      docHeight: document.documentElement.scrollHeight,
      bodyFont: getComputedStyle(document.body).fontSize,
      h1Count: h1s.length,
      h1: h1s[0]
        ? h1s[0].textContent.trim().replace(/\s+/g, " ")
        : "",
      subtitleCount: all(
        "#title-block-header .subtitle, .quarto-title .subtitle"
      ).filter(shown).length,
      metaCount: all(".chapter-meta").filter(shown).length,
      kickerCount: all(".chapter-kicker, .kicker").filter(shown).length,
      widgetSvgCount: widgetSvgs.length,
      widgetSvgWidths: widgetSvgMetrics.map((metric) => metric.width),
      widgetSvgMetrics,
      widgetControlCount: all(
        ".widget-frame input, .widget-frame select, .widget-frame textarea"
      ).length,
      genericPanelLabel: text.includes("Parametri simulacije"),
      staleText: /STATUS:\s*kostur|Naslov prvog odjeljka|Interaktivni graf još nije izrađen/.test(
        text
      ),
      literalNull: all("main *, #quarto-content *").some(
        (element) => shown(element) &&
          !element.closest("code, pre, .sourceCode, .cell-code") &&
          element.children.length === 0 &&
          (element.textContent || "").trim().toLowerCase() === "null"
      ),
      englishUi:
        /\b(?:Table of contents|Appendix [A-G]|Source Code|No results|Matching documents|Clear search|Cancel search|Submit search|Search this site)\b/i.test(text) ||
        /\b(?:Search|Share|Source Code|Toggle navigation|Toggle dark mode|Toggle light mode|Toggle reader mode|No results|Matching documents|Clear search|Cancel search|Submit search)\b/i.test(
          uiAttributeText
        ),
      brokenImages: images
        .filter((image) => !image.complete || image.naturalWidth === 0)
        .map((image) => image.getAttribute("src")),
      ojsErrors: all(".observablehq--error, .observablehq--inspect")
        .filter(
          (element) => shown(element) &&
            /error|exception|undefined is not|not defined/i.test(
              element.textContent || ""
            )
        )
        .map((element) => (element.textContent || "").trim().slice(0, 300)),
      callouts,
      tables,
      lightFigures: all(".figure-theme-light").filter(shown).length,
      darkFigures: all(".figure-theme-dark").filter(shown).length,
      hasPairs: all(".figure-theme-light, .figure-theme-dark").length > 0,
      headerHeight: header && shown(header) ? boxOf(header).height : 0,
      navbarUtilityIcons,
      sidebarVisible: shown(sidebar),
      pagerVisible: shown(pager),
      standalone: document.body.classList.contains("standalone-page"),
    };
  }, {
    currentRoute: route,
    currentWidth: width,
    currentTheme: theme,
  });
}

function evaluateFailures(result, failures) {
  const add = (issue) => failures.push({
    theme: result.theme,
    width: result.width,
    route: result.route,
    issue,
  });

  if (result.status !== 200) add(`HTTP ${result.status}`);
  if (result.docWidth > result.width + 1) {
    add(`document overflow ${result.docWidth}>${result.width}`);
  }
  if (result.staleText) add("stale visible text");
  if (result.literalNull) add("literal null visible");
  if (result.englishUi) add("English interface text visible");
  if (result.brokenImages.length) {
    add(`broken images: ${result.brokenImages.join(", ")}`);
  }
  if (result.ojsErrors.length) add(`OJS error: ${result.ojsErrors.join(" | ")}`);
  if (result.consoleErrors.length) add(result.consoleErrors.join(" | "));
  if (result.bodyFont !== "17px") add(`body font ${result.bodyFont}`);

  if (isNumberedChapter(result.route)) {
    if (!result.subtitleCount) add("missing subtitle");
    if (!result.metaCount) add("missing chapter meta");
    if (!result.kickerCount) add("missing chapter kicker");
  }
  if (needsWidget(result.route)) {
    if (!result.widgetSvgCount) add("widget SVG missing");
    if (!result.widgetControlCount) add("widget controls missing");
    if (result.genericPanelLabel) add("generic widget panel label");
    for (const metric of result.widgetSvgMetrics) {
      if (
        metric.minEffectiveText !== null &&
        metric.minEffectiveText < 10.5
      ) {
        add(
          `widget SVG text too small ${metric.minEffectiveText.toFixed(1)}px`
        );
      }
    }
  }

  for (const callout of result.callouts) {
    if (callout.box.x < -1 || callout.box.right > result.width + 1) {
      add(`${callout.kind} outside viewport`);
    }
    if (callout.scrollWidth > callout.clientWidth + 1) {
      add(`${callout.kind} internal overflow`);
    }
    if (
      callout.firstTextX !== null &&
      callout.firstTextX < callout.box.x - 1
    ) {
      add(`${callout.kind} text clips label edge`);
    }
    if (result.width >= 1000 && callout.box.width > 760) {
      add(`${callout.kind} over-wide ${callout.box.width.toFixed(1)}`);
    }
  }

  for (const table of result.tables) {
    if (!table.needsScroll) continue;
    if (!table.hasScroller) add("wide table lacks scroll container");
    if (!table.scrollerFocusable) add("wide table scroller is not focusable");
    if (!table.scrollerLabelled) add("wide table scroller lacks accessible name");
    if (!table.hintVisible) add("wide table lacks visible scroll cue");
    if (!table.firstColumnSticky) add("wide table lacks sticky first column");
  }

  if (result.hasPairs) {
    if (result.theme === "light" && result.darkFigures) {
      add("dark figure visible in light theme");
    }
    if (result.theme === "dark" && result.lightFigures) {
      add("light figure visible in dark theme");
    }
    if (result.theme === "light" && !result.lightFigures) {
      add("light paired figure missing");
    }
    if (result.theme === "dark" && !result.darkFigures) {
      add("dark paired figure missing");
    }
  }

  if (result.width <= 600 && result.headerHeight > 95) {
    add(`mobile header too tall ${result.headerHeight.toFixed(1)}`);
  }
  if (result.width === 1000 && result.headerHeight > 70) {
    add(`compact desktop header too tall ${result.headerHeight.toFixed(1)}`);
  }
  if (result.width >= 992) {
    for (const [name, icon] of Object.entries(result.navbarUtilityIcons || {})) {
      if (!icon || !icon.visible || icon.opacity <= 0) {
        add(`${name} navbar utility icon is not visible`);
        continue;
      }
      if (
        icon.backgroundImage !== "none" ||
        icon.maskImage === "none" ||
        icon.backgroundColor === "rgba(0, 0, 0, 0)"
      ) {
        add(`${name} navbar utility icon is not token-painted`);
      }
    }
  }
  if (isStandalone(result.route)) {
    if (!result.standalone) add("standalone class missing");
    if (result.sidebarVisible) add("sidebar visible on standalone page");
    if (result.pagerVisible) add("pager visible on standalone page");
  }
  if (
    (result.route === "/" || result.route === "/index.html") &&
    result.h1Count !== 1
  ) {
    add(`landing H1 count ${result.h1Count}`);
  }
  if (
    result.route === "/references.html" &&
    /Appendix|Dodatak\s+[A-G]/i.test(result.h1)
  ) {
    add("Literature mislabeled as appendix");
  }

  const appendixExpected = {
    "/dodaci/a-praktikum.html": "Dodatak A",
    "/dodaci/b-jamovi.html": "Dodatak B",
    "/dodaci/c-katalog-podataka.html": "Dodatak C",
    "/dodaci/d-koji-test.html": "Dodatak D",
    "/dodaci/e-rjecnik.html": "Dodatak E",
    "/dodaci/f-ai-protokol.html": "Dodatak F",
  }[result.route];
  if (appendixExpected && !result.h1.startsWith(appendixExpected)) {
    add(`appendix title mismatch: ${result.h1}`);
  }
}

async function main() {
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({
    headless: true,
    executablePath:
      "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  });
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    reducedMotion: "reduce",
  });
  const page = await context.newPage();
  let consoleErrors = [];

  page.on("console", (message) => {
    if (message.type() === "error") {
      consoleErrors.push(`console: ${message.text()}`);
    }
  });
  page.on("pageerror", (error) => {
    consoleErrors.push(`pageerror: ${error.message}`);
  });

  const metrics = [];
  const failures = [];
  let screenshotCount = 0;

  for (const theme of auditedThemes) {
    for (const width of auditedWidths) {
      await page.setViewportSize({
        width,
        height: width <= 600 ? 844 : 900,
      });

      for (const [route, label] of auditedRoutes) {
        consoleErrors = [];
        let resultRecorded = false;
        try {
          const response = await page.goto(`${base}${route}`, {
            waitUntil: "domcontentloaded",
            timeout: 20000,
          });
          await page.evaluate(async () => {
            if (document.fonts && document.fonts.ready) {
              await document.fonts.ready;
            }
          });
          await page.evaluate((desired) => {
            const dark = document.body.classList.contains("quarto-dark");
            if (
              (desired === "dark") !== dark &&
              typeof window.quartoToggleColorScheme === "function"
            ) {
              window.quartoToggleColorScheme();
            }
          }, theme);
          await page.waitForFunction(
            (desired) => document.body.classList.contains(
              desired === "dark" ? "quarto-dark" : "quarto-light"
            ),
            theme,
            { timeout: 5000 }
          );

          if (needsWidget(route)) {
            await page.waitForFunction(
              () => document.querySelectorAll(".widget-frame svg").length > 0 ||
                document.querySelectorAll(".observablehq--error").length > 0,
              null,
              { timeout: 8000 }
            ).catch(() => {});
          } else {
            await page.waitForTimeout(250);
          }
          await page.waitForTimeout(200);

          const result = await collectMetrics(page, route, width, theme);
          result.status = response ? response.status() : null;
          result.consoleErrors = [...new Set(consoleErrors)];
          metrics.push(result);
          resultRecorded = true;
          evaluateFailures(result, failures);

          if (screenshotWidths.has(width)) {
            screenshotCount += await captureAuditScreenshot(
              page,
              path.join(outDir, `${theme}_${width}_${label}.jpg`)
            );
          }
        } catch (error) {
          failures.push({
            theme,
            width,
            route,
            issue: `audit exception: ${error.message}`,
          });
          if (!resultRecorded) {
            metrics.push({
              theme,
              width,
              route,
              fatal: error.message,
              consoleErrors,
            });
          }
        }
      }
    }
  }

  fs.writeFileSync(
    path.join(outDir, "metrics.json"),
    JSON.stringify({ metrics, failures }, null, 2)
  );
  console.log(`AUDIT_DIR=${outDir}`);
  console.log(
    `ROUTES=${auditedRoutes.length} CASES=${metrics.length} FAILURES=${failures.length}`
  );
  console.log(`SCREENSHOTS=${screenshotCount}`);
  for (const failure of failures.slice(0, 150)) {
    console.log(JSON.stringify(failure));
  }
  await browser.close();
  if (failures.length && process.env.AUDIT_ALLOW_FAILURES !== "1") {
    process.exitCode = 1;
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
