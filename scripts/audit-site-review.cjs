// Final website regression audit. Run after rendering: node scripts/audit-site-review.cjs docs
// AUDIT_BASE optionally targets a deployed copy instead of starting a local server.
const { chromium } = require("playwright");
const fs = require("node:fs");
const path = require("node:path");
const http = require("node:http");
const assert = require("node:assert/strict");
const root = path.resolve(process.argv[2] || "docs");
const inventory = require("../config/book-inventory.json");
const server = http.createServer((req, res) => {
  let pathname = decodeURIComponent(
    new URL(req.url, "http://localhost").pathname,
  );
  if (pathname.endsWith("/")) pathname += "index.html";
  const file = path.resolve(root, "." + pathname);
  if (!file.startsWith(root + path.sep)) {
    res.writeHead(403).end();
    return;
  }
  fs.readFile(file, (error, data) => {
    if (error) {
      res.writeHead(404).end();
      return;
    }
    res.setHeader(
      "Content-Type",
      {
        ".html": "text/html",
        ".js": "text/javascript",
        ".css": "text/css",
        ".json": "application/json",
        ".svg": "image/svg+xml",
      }[path.extname(file)] || "application/octet-stream",
    );
    res.end(data);
  });
});
(async () => {
  await new Promise((r) => server.listen(0, "127.0.0.1", r));
  const base =
    process.env.AUDIT_BASE || `http://127.0.0.1:${server.address().port}/`;
  const browser = await chromium.launch();
  const errors = [],
    failures = [];
  try {
    const context = await browser.newContext({
      viewport: { width: 1440, height: 1000 },
      permissions: ["clipboard-read", "clipboard-write"],
    });
    const p = await context.newPage();
    p.on("pageerror", (e) => errors.push(e.message));
    const go = async (route) => {
      assert.equal((await p.goto(base + route)).status(), 200, route);
      await p.locator(".site-search-button").waitFor();
    };
    await go("index.html");
    assert.equal(await p.locator(".landing-distribution").count(), 0);
    for (const file of ["cv-luka.html", "cv-petra.html"])
      assert.equal(
        await p.locator(`.landing-authors a[href$="${file}"]`).count(),
        1,
      );
    assert.equal(await p.locator(".site-footer-links a").count(), 3);
    for (const route of [
      "index.html",
      "podaci.html",
      "uci-s-ai.html",
      "chapters/13-kategoricki-podaci.html",
    ]) {
      await go(route);
      for (const width of [1440, 390]) {
        await p.setViewportSize({ width, height: 1000 });
        const search = p.getByRole("button", {
          name: "Pretraži knjigu",
          exact: true,
        });
        assert.equal(await search.count(), 1, route + " single search button");
        await search.click();
        const input = p.locator(".aa-DetachedOverlay .aa-Input");
        await input.fill("regresija");
        await p.locator(".aa-DetachedOverlay .aa-Item").first().waitFor();
        await p.keyboard.press("Escape");
        await input.waitFor({ state: "hidden" });
        assert(
          await search.evaluate((e) => document.activeElement === e),
          route + " search focus return",
        );
      }
    }
    await p.setViewportSize({ width: 1440, height: 1000 });
    await p
      .getByRole("button", { name: "Pretraži knjigu", exact: true })
      .click();
    await p.locator(".aa-DetachedOverlay .aa-Input").fill("regresija");
    await p.locator(".aa-DetachedOverlay .aa-Item a").first().waitFor();
    const resultURL = await p
      .locator(".aa-DetachedOverlay .aa-Item a")
      .first()
      .getAttribute("href");
    await p.locator(".aa-DetachedOverlay .aa-Item a").first().click();
    await p.waitForURL(new URL(resultURL, base).href);
    await go("chapters/13-kategoricki-podaci.html");
    for (const page of inventory.pages.filter((x) =>
      /^chapters\//.test(x.output),
    )) {
      const a = p
        .locator(
          `#quarto-sidebar a.sidebar-link[href$="${path.basename(page.output)}"]`,
        )
        .first();
      assert.equal(await a.count(), 1, page.output + " sidebar link");
      assert(
        await a.evaluate(
          (e) =>
            e.style.display !== "none" &&
            e.closest(".sidebar-item").style.display !== "none",
        ),
        page.output + " not pruned",
      );
    }
    await p.locator(".quarto-reader-toggle").click();
    await p.waitForFunction(() =>
      document.body.classList.contains("site-reading-focus"),
    );
    assert(!(await p.locator("#quarto-sidebar").isVisible()));
    assert(
      await p.locator("main").evaluate((e) => {
        const r = e.getBoundingClientRect(),
          h = e.querySelector("#title-block-header").getBoundingClientRect();
        return (
          Math.abs((r.left + r.right) / 2 - innerWidth / 2) < 2 &&
          Math.abs(h.left - r.left) < 2 &&
          document.documentElement.scrollWidth <= innerWidth + 2
        );
      }),
      "reading mode centered without overflow",
    );
    await p.locator(".quarto-reader-toggle").click();
    await go("podaci.html");
    assert(await p.locator("h1.title").isVisible());
    assert((await p.locator(".dataset-entry").count()) > 0);
    assert(!(await p.locator(".catalogue-reference").getAttribute("open")));
    await p.locator(".catalogue-controls input").fill("NEPOSTOJEĆI-SKUP");
    assert.equal(await p.locator(".dataset-entry:visible").count(), 0);
    await p.locator(".catalogue-controls input").fill("mreže");
    assert((await p.locator(".dataset-entry:visible").count()) > 0);
    const chapter = p.locator(".catalogue-controls select");
    assert((await chapter.locator("option").count()) > 2);
    await p.locator(".catalogue-controls input").fill("");
    await chapter.selectOption({ index: 1 });
    assert((await p.locator(".dataset-entry:visible").count()) > 0);
    await go("rjesenja.html#sol-16-callout-greska-01");
    assert.equal(await p.locator("main > section.level1:visible").count(), 1);
    assert(await p.locator("#sol-16-callout-greska-01").isVisible());
    assert((await p.locator(".solution-tasks a").count()) > 0);
    await p.locator(".solution-picker select").selectOption({ index: 2 });
    assert(!(await p.locator("#sol-16-callout-greska-01").isVisible()));
    await go("uci-s-ai.html");
    await p.locator(".ai-selection").waitFor();
    assert(await p.locator(".ojs-task-control select").isVisible());
    await p.locator(".ojs-task-control select").selectOption({ index: 5 });
    await p.waitForFunction(() =>
      document
        .querySelector(".ai-selection a[download]")
        .getAttribute("href")
        .includes("05-"),
    );
    assert(!/\b0k\b|NaN/.test(await p.locator(".ai-file-note").innerText()));
    await go("dodaci/a-praktikum.html");
    assert.equal(
      await p.locator(".navbar-nav a.active").innerText(),
      "Praktikum",
    );
    assert.equal(await p.locator(".practice-paths a").count(), 2);
    await go("404.html");
    assert(
      (
        await p
          .getByRole("link", { name: "Prvo poglavlje", exact: true })
          .getAttribute("href")
      ).includes("01-zasto-statistika"),
    );
    await go("pojmovnik.html");
    await p.locator(".atlas-node").first().waitFor();
    assert.equal(await p.locator('.atlas-node[tabindex="0"]').count(), 1);
    await p.locator('.atlas-node[tabindex="0"]').focus();
    const before = await p.evaluate(() =>
      document.activeElement.getAttribute("aria-label"),
    );
    await p.keyboard.press("ArrowRight");
    assert.notEqual(
      await p.evaluate(() => document.activeElement.getAttribute("aria-label")),
      before,
    );
    await p.keyboard.press("Enter");
    assert(await p.locator(".atlas-definition").isVisible());
    await p.getByRole("button", { name: "Modeli", exact: true }).click();
    assert(!(await p.locator(".atlas-definition").isVisible()));
    for (let theme = 0; theme < 2; theme++) {
      const category = p.getByRole("button", { name: "Modeli", exact: true });
      await category.hover();
      const contrast = await category.evaluate((e) => {
        const luminance = (color) => {
          const rgb = color
            .match(/[\d.]+/g)
            .slice(0, 3)
            .map(Number)
            .map((v) => {
              v /= 255;
              return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
            });
          return rgb[0] * 0.2126 + rgb[1] * 0.7152 + rgb[2] * 0.0722;
        };
        const style = getComputedStyle(e),
          a = luminance(style.color),
          b = luminance(style.backgroundColor);
        return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
      });
      assert(contrast >= 4.5, "atlas hover contrast " + contrast);
      await p.locator(".quarto-color-scheme-toggle").click();
    }
    await p.setViewportSize({ width: 390, height: 844 });
    await p.locator(".atlas-node").first().click({ force: true });
    await p.waitForTimeout(400);
    assert(
      await p.locator(".atlas-definition h2").evaluate((e) => {
        const r = e.getBoundingClientRect();
        return r.top >= 0 && r.bottom < innerHeight;
      }),
      "mobile definition visible",
    );
    console.log(
      "SITE_TASKS_OK search sidebar reader data solutions ai practicum recovery atlas",
    );

    // Every sanctioned route, both themes, and narrow/desktop layouts. Wide content
    // may scroll inside a labelled region but may not widen the document.
    const routes = ["", ...inventory.pages.map((x) => x.output)];
    let cases = 0;
    for (const theme of ["light", "dark"]) {
      await p.evaluate(
        (theme) => localStorage.setItem("quarto-color-scheme", theme),
        theme,
      );
      for (const route of routes) {
        await go(route);
        await p.waitForTimeout(200);
        for (const width of [1440, 390, 320]) {
          await p.setViewportSize({ width, height: 1000 });
          await p.waitForTimeout(120);
          const result = await p.evaluate(() => ({
            width: document.documentElement.scrollWidth,
            errors: [...document.querySelectorAll(".observablehq--error")].map(
              (e) => e.textContent,
            ),
            tables: [...document.querySelectorAll("main table")]
              .filter(
                (t) =>
                  t.getBoundingClientRect().width > 0 &&
                  t.scrollWidth > t.parentElement.clientWidth + 2,
              )
              .filter(
                (t) =>
                  !t.closest(".table-scrollable") ||
                  t.closest(".table-scrollable").nextElementSibling?.hidden,
              ).length,
          }));
          if (result.width > width + 2 || result.errors.length || result.tables)
            failures.push({ route, theme, viewport: width, ...result });
          cases++;
        }
      }
    }
    assert.deepEqual(errors, [], "JavaScript errors");
    assert.deepEqual(failures, [], "rendering regressions");
    console.log(
      `SITE_REVIEW_OK cases=${cases} routes=${routes.length} themes=2 widths=3`,
    );
  } finally {
    await browser.close();
    await new Promise((r) => server.close(r));
  }
})().catch((e) => {
  console.error(e);
  server.close();
  process.exitCode = 1;
});
