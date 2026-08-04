/* Browser audit for the rendered HTML book.
 *
 * Blocking smoke audit (starts its own local server):
 *   node scripts/audit-rendered-html.js --smoke --root docs
 *
 * Complete manual audit (expects an existing local server):
 *   $env:AUDIT_BASE = "http://127.0.0.1:8899"
 *   node scripts/audit-rendered-html.js
 *
 * Both modes resolve the committed Playwright package from this checkout and
 * launch the Chromium revision installed for that package. The complete mode
 * checks every canonical route at seven widths in both themes and retains
 * screenshots; it remains a manual diagnostic rather than the release smoke
 * gate.
 */

"use strict";

const fs = require("fs");
const http = require("http");
const os = require("os");
const path = require("path");

const root = path.resolve(__dirname, "..");
const inventoryPath = path.join(root, "config", "book-inventory.json");
if (!fs.existsSync(inventoryPath)) {
  throw new Error("missing canonical inventory: config/book-inventory.json");
}
const bookInventory = JSON.parse(fs.readFileSync(inventoryPath, "utf8"));
if (
  bookInventory.schema_version !== 1 ||
  bookInventory.inventory !== "sanctioned-book-pages-and-routes" ||
  !Array.isArray(bookInventory.pages)
) {
  throw new Error("invalid canonical book inventory");
}
if (!Array.isArray(bookInventory.public_aliases)) {
  throw new Error("canonical book inventory has no public alias inventory");
}
const pageById = new Map(bookInventory.pages.map((page) => [page.id, page]));
const rootAlias = bookInventory.public_aliases.find((alias) => alias.path === "/");
if (!rootAlias || !pageById.has(rootAlias.page)) {
  throw new Error("canonical book inventory has no valid root alias");
}
const pageByRoute = new Map([
  ...bookInventory.pages.map((page) => [`/${page.output}`, page]),
  ...bookInventory.public_aliases.map((alias) => [alias.path, pageById.get(alias.page)]),
]);
const localPlaywrightPath = path.join(root, "node_modules", "playwright");
const localPlaywrightManifest = path.join(localPlaywrightPath, "package.json");
if (!fs.existsSync(localPlaywrightManifest)) {
  throw new Error(
    "missing committed Playwright installation; run python scripts/restore-dependencies.py"
  );
}
const { chromium } = require(localPlaywrightPath);

function parseCommandLine(argv) {
  const options = {
    mode: "complete",
    root: "docs",
    fixture: null,
  };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--smoke") {
      options.mode = "smoke";
    } else if (argument === "--root") {
      index += 1;
      if (!argv[index]) throw new Error("--root requires a directory");
      options.root = argv[index];
    } else if (argument === "--fixture") {
      index += 1;
      if (argv[index] !== "missing-route") {
        throw new Error("--fixture supports only missing-route");
      }
      options.fixture = argv[index];
    } else {
      throw new Error(`unknown argument: ${argument}`);
    }
  }
  if (options.mode !== "smoke" && options.fixture) {
    throw new Error("--fixture is available only with --smoke");
  }
  return options;
}

const commandLine = parseCommandLine(process.argv.slice(2));

const base = process.env.AUDIT_BASE || "http://127.0.0.1:8899";
const outDir = process.env.AUDIT_DIR || (
  commandLine.mode === "complete"
    ? fs.mkdtempSync(path.join(os.tmpdir(), "statistika-postfix-audit-"))
    : null
);

const routes = [
  ...bookInventory.public_aliases.map((alias) => [alias.path, alias.audit_label]),
  ...bookInventory.pages.map((page) => [`/${page.output}`, page.audit_label]),
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
  return pageByRoute.get(route)?.kind === "chapter";
}

function needsWidget(route) {
  return pageByRoute.get(route)?.widget === true;
}

function isStandalone(route) {
  if (route === "/") return true;
  return pageByRoute.get(route)?.standalone === true;
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
    pageByRoute.get(result.route)?.kind === "landing" &&
    result.h1Count !== 1
  ) {
    add(`landing H1 count ${result.h1Count}`);
  }
  if (
    pageByRoute.get(result.route)?.kind === "references" &&
    /Appendix|Dodatak\s+[A-G]/i.test(result.h1)
  ) {
    add("Literature mislabeled as appendix");
  }

  const appendix = pageByRoute.get(result.route);
  const appendixExpected = appendix?.kind === "appendix"
    ? `Dodatak ${appendix.appendix_letter}`
    : null;
  if (appendixExpected && !result.h1.startsWith(appendixExpected)) {
    add(`appendix title mismatch: ${result.h1}`);
  }
}

function verifyLockedBrowserRuntime() {
  const packageManifest = JSON.parse(
    fs.readFileSync(path.join(root, "package.json"), "utf8")
  );
  const packageLock = JSON.parse(
    fs.readFileSync(path.join(root, "package-lock.json"), "utf8")
  );
  const nodePin = fs.readFileSync(path.join(root, ".node-version"), "utf8").trim();
  const installedManifest = JSON.parse(
    fs.readFileSync(localPlaywrightManifest, "utf8")
  );
  const expectedPlaywright = packageManifest.devDependencies?.playwright;
  const lockedRoot = packageLock.packages?.[""];
  const lockedPlaywright = packageLock.packages?.["node_modules/playwright"];
  const playwrightCoreBrowsers = JSON.parse(
    fs.readFileSync(
      path.join(root, "node_modules", "playwright-core", "browsers.json"),
      "utf8"
    )
  );
  const chromiumRecord = playwrightCoreBrowsers.browsers.find(
    (browser) => browser.name === "chromium"
  );

  if (!/^\d+\.\d+\.\d+$/.test(expectedPlaywright || "")) {
    throw new Error("package.json must pin one exact Playwright version");
  }
  if (packageLock.lockfileVersion !== 3) {
    throw new Error("package-lock.json must use lockfileVersion 3");
  }
  if (
    lockedRoot?.devDependencies?.playwright !== expectedPlaywright ||
    lockedPlaywright?.version !== expectedPlaywright ||
    !lockedPlaywright?.integrity ||
    installedManifest.version !== expectedPlaywright
  ) {
    throw new Error("committed and installed Playwright versions do not agree");
  }
  if (process.version.replace(/^v/, "") !== nodePin) {
    throw new Error(
      `Node version mismatch: expected ${nodePin}, found ${process.version}`
    );
  }
  if (!chromiumRecord?.revision) {
    throw new Error("installed Playwright package does not declare Chromium");
  }
  const executable = chromium.executablePath();
  if (!fs.existsSync(executable)) {
    throw new Error(
      `missing Playwright Chromium; run python scripts/restore-dependencies.py: ${executable}`
    );
  }
  return {
    executable,
    node: nodePin,
    playwright: expectedPlaywright,
    chromiumRevision: chromiumRecord.revision,
  };
}

function mimeType(filePath) {
  return {
    ".css": "text/css; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".ico": "image/x-icon",
    ".jpeg": "image/jpeg",
    ".jpg": "image/jpeg",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".png": "image/png",
    ".svg": "image/svg+xml",
    ".woff": "font/woff",
    ".woff2": "font/woff2",
  }[path.extname(filePath).toLowerCase()] || "application/octet-stream";
}

async function startStaticServer(renderRoot) {
  const resolvedRoot = path.resolve(renderRoot);
  if (!fs.statSync(resolvedRoot, { throwIfNoEntry: false })?.isDirectory()) {
    throw new Error(`rendered HTML root does not exist: ${resolvedRoot}`);
  }
  const server = http.createServer((request, response) => {
    let pathname;
    try {
      pathname = decodeURIComponent(
        new URL(request.url || "/", "http://127.0.0.1").pathname
      );
    } catch {
      response.writeHead(400).end("Bad request");
      return;
    }
    if (pathname === "/") pathname = `/${pageById.get(rootAlias.page).output}`;
    const requestedPath = path.resolve(resolvedRoot, `.${pathname}`);
    if (
      requestedPath !== resolvedRoot &&
      !requestedPath.startsWith(`${resolvedRoot}${path.sep}`)
    ) {
      response.writeHead(403).end("Forbidden");
      return;
    }
    const stat = fs.statSync(requestedPath, { throwIfNoEntry: false });
    if (!stat?.isFile()) {
      response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      response.end("Not found");
      return;
    }
    response.writeHead(200, { "Content-Type": mimeType(requestedPath) });
    const stream = fs.createReadStream(requestedPath);
    stream.on("error", () => response.destroy());
    stream.pipe(response);
  });
  await new Promise((resolve, reject) => {
    server.once("error", reject);
    server.listen(0, "127.0.0.1", resolve);
  });
  const address = server.address();
  if (!address || typeof address === "string") {
    server.close();
    throw new Error("could not determine browser smoke server address");
  }
  return {
    baseUrl: `http://127.0.0.1:${address.port}`,
    server,
  };
}

async function runSmokeAudit() {
  const runtime = verifyLockedBrowserRuntime();
  const renderedRoot = path.resolve(root, commandLine.root);
  const { baseUrl, server } = await startStaticServer(renderedRoot);
  const smokePage = bookInventory.pages.find((page) => page.browser_smoke === true);
  if (!smokePage) throw new Error("canonical inventory has no browser smoke page");
  const smokeRoute = commandLine.fixture === "missing-route"
    ? "/__p1c_browser_missing_route__.html"
    : `/${smokePage.output}`;
  let browser;
  try {
    browser = await chromium.launch({ headless: true });
    const context = await browser.newContext({
      viewport: { width: 1280, height: 900 },
      deviceScaleFactor: 1,
      reducedMotion: "reduce",
      colorScheme: "light",
    });
    const page = await context.newPage();
    const pageErrors = [];
    page.on("pageerror", (error) => pageErrors.push(error.message));

    const response = await page.goto(`${baseUrl}${smokeRoute}`, {
      waitUntil: "domcontentloaded",
      timeout: 20000,
    });
    const status = response?.status() || 0;
    if (status !== 200) {
      throw new Error(`browser path returned HTTP ${status}: ${smokeRoute}`);
    }

    const widget = page.locator(".widget-frame").first();
    const details = widget.locator("details.ojs-collapsible").first();
    const summary = details.locator("summary").first();
    const slider = details.locator('input[type="range"]').first();
    const reset = details.locator("button.ojs-reset").first();
    const liveRegion = widget.locator(
      '.widget-foot[role="status"][aria-live="polite"]'
    ).first();
    const figure = widget.locator("svg:not(.observablehq--caret)").first();

    await figure.waitFor({ state: "visible", timeout: 20000 });
    await summary.waitFor({ state: "visible", timeout: 10000 });
    if (await details.evaluate((element) => element.open)) {
      throw new Error("widget control panel must start collapsed");
    }
    await summary.focus();
    await page.keyboard.press("Enter");
    await details.evaluate((element) => {
      if (!element.open) throw new Error("keyboard did not open control panel");
    });
    await slider.waitFor({ state: "visible", timeout: 10000 });
    await reset.waitFor({ state: "visible", timeout: 10000 });
    await liveRegion.waitFor({ state: "visible", timeout: 10000 });

    const initialValue = await slider.inputValue();
    const range = await slider.evaluate((element) => ({
      maximum: Number(element.max),
      minimum: Number(element.min),
      step: Number(element.step || 1),
      value: Number(element.value),
    }));
    const key = range.value + range.step <= range.maximum
      ? "ArrowRight"
      : "ArrowLeft";
    await slider.focus();
    await page.keyboard.press(key);
    await page.waitForTimeout(300);
    const changedValue = await slider.inputValue();
    if (changedValue === initialValue) {
      throw new Error(`keyboard ${key} did not change the widget control`);
    }
    if (!(await liveRegion.getAttribute("aria-live"))?.includes("polite")) {
      throw new Error("widget result is not exposed as a polite live region");
    }
    if (!(await liveRegion.textContent())?.trim()) {
      throw new Error("widget live region is empty after interaction");
    }

    await reset.focus();
    await page.keyboard.press("Enter");
    await page.waitForTimeout(300);
    if (await slider.inputValue() !== initialValue) {
      throw new Error("keyboard reset did not restore the initial value");
    }

    const themeToggle = page.locator(".quarto-color-scheme-toggle").first();
    await themeToggle.waitFor({ state: "visible", timeout: 10000 });
    await themeToggle.focus();
    await page.keyboard.press("Enter");
    await page.waitForFunction(
      () => document.body.classList.contains("quarto-dark"),
      null,
      { timeout: 5000 }
    );

    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(250);
    const responsive = await widget.evaluate((element) => {
      const box = element.getBoundingClientRect();
      return {
        documentWidth: document.documentElement.scrollWidth,
        right: box.right,
        viewportWidth: window.innerWidth,
        width: box.width,
      };
    });
    if (
      responsive.documentWidth > responsive.viewportWidth + 1 ||
      responsive.right > responsive.viewportWidth + 1 ||
      responsive.width <= 0
    ) {
      throw new Error(
        `responsive overflow at 390px: document=${responsive.documentWidth} widgetRight=${responsive.right}`
      );
    }
    if (pageErrors.length) {
      throw new Error(`browser page error: ${[...new Set(pageErrors)].join(" | ")}`);
    }

    console.log(
      "BROWSER_RUNTIME_OK " +
      `node=${runtime.node} playwright=${runtime.playwright} ` +
      `chromium_revision=${runtime.chromiumRevision} executable=${runtime.executable}`
    );
    console.log(
      "BROWSER_SMOKE_OK " +
      `route=${smokeRoute} widths=1280,390 themes=light,dark ` +
      "keyboard=pass reset=pass live_region=pass publish=false"
    );
    await context.close();
  } finally {
    if (browser) await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
}

async function runCompleteAudit() {
  verifyLockedBrowserRuntime();
  fs.mkdirSync(outDir, { recursive: true });
  const browser = await chromium.launch({ headless: true });
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

const selectedAudit = commandLine.mode === "smoke"
  ? runSmokeAudit
  : runCompleteAudit;

selectedAudit().catch((error) => {
  console.error(
    `BROWSER_AUDIT_FAILED mode=${commandLine.mode} ` +
    `fixture=${commandLine.fixture || "none"}: ${error.message}`
  );
  process.exit(1);
});
