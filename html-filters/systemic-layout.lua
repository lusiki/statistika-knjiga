-- HTML-only structural repairs for the book layout.
--
-- Quarto promotes every ancestor of a margin citation to `.page-full`.
-- That is useful for ordinary prose because it creates a margin track, but it
-- is destructive for the four pedagogical callouts: their decoration is then
-- painted across the viewport and can begin behind the docked sidebar.
--
-- Quarto materialises margin citations after the Pandoc AST has been finalised.
-- The injected script therefore repairs that generated DOM once parsing is
-- complete: it moves non-empty margin containers next to their callout,
-- removes empty ones, and returns the semantic callout to the reading column.

local function layout_script()
  return pandoc.RawBlock("html", [[
<script>
(function () {
  var chapterMatch = window.location.pathname.match(
    /\/chapters\/(0[1-9]|1[0-8])-[^/]+\.html$/
  );
  var title = document.querySelector("#title-block-header h1.title");
  if (chapterMatch && title && !title.parentNode.querySelector(".chapter-kicker")) {
    // Sustav Zvono: disk s brojem i os lijevo, oznaka dijela iznad naslova.
    var header = document.getElementById("title-block-header");
    if (header) header.classList.add("zv-opener");

    var rail = document.createElement("span");
    rail.className = "zv-rail";
    rail.setAttribute("aria-hidden", "true");
    var disc = document.createElement("span");
    disc.className = "zv-rail__disc";
    disc.textContent = chapterMatch[1];
    rail.appendChild(disc);
    title.parentNode.insertBefore(rail, title.parentNode.firstChild);

    var partLink = document.querySelector(
      "#title-block-header .breadcrumb .breadcrumb-item:first-child a"
    );
    var partName = "";
    if (partLink) {
      var raw = partLink.textContent.trim();
      var m = raw.match(/^DIO ([IVX]+):\s*(.+)$/);
      partName = m
        ? "Dio " + m[1] + " · " + m[2].charAt(0) + m[2].slice(1).toLowerCase()
        : raw.charAt(0) + raw.slice(1).toLowerCase();
    }
    var kicker = document.createElement("span");
    kicker.className = "kicker chapter-kicker";
    kicker.textContent = "Poglavlje " + parseInt(chapterMatch[1], 10) +
      (partName ? " · " + partName : "");
    title.parentNode.insertBefore(kicker, title);
  }

  function repairGeneratedLayout() {
    var selector = [
      ".callout-vinjeta",
      ".callout-divljina",
      ".callout-model",
      ".callout-greska"
    ].join(",");

    document.querySelectorAll(selector).forEach(function (callout) {
      callout.classList.remove("page-full", "page-columns");
      // A cited table can carry its own nested page grid. Keep its caption and
      // cells in the callout's reading column as well.
      callout.querySelectorAll(".page-full, .page-columns").forEach(function (node) {
        node.classList.remove("page-full", "page-columns");
      });

      var insertionPoint = callout;
      callout.querySelectorAll(".column-margin").forEach(function (child) {
        insertionPoint.parentNode.insertBefore(child, insertionPoint.nextSibling);
        insertionPoint = child;
      });
    });

    /*
     * Margin citations can promote a complete paired figure—and every wrapper
     * inside it—to Quarto's full-page grid. Besides escaping the viewport on
     * narrow screens, `.page-columns { display: grid }` then defeats the
     * light/dark visibility rule. Paired figures belong to the reading column;
     * their caption's margin citation is moved separately by Quarto.
     */
    document.querySelectorAll(".quarto-float").forEach(function (figure) {
      if (!figure.querySelector(".figure-theme-light, .figure-theme-dark")) return;
      [figure].concat(Array.from(
        figure.querySelectorAll(".page-full, .page-columns")
      )).forEach(function (node) {
        node.classList.remove("page-full", "page-columns");
      });
    });

    document.querySelectorAll(".column-margin").forEach(function (margin) {
      if (!margin.textContent.trim() && margin.children.length === 0) {
        margin.remove();
      }
    });
  }

  function revealActiveBookItem() {
    var sidebar = document.getElementById("quarto-sidebar");
    var active = sidebar && sidebar.querySelector(".sidebar-link.active");
    if (!sidebar || !active || sidebar.scrollHeight <= sidebar.clientHeight) return;

    var sidebarBox = sidebar.getBoundingClientRect();
    var activeBox = active.getBoundingClientRect();
    if (activeBox.top >= sidebarBox.top && activeBox.bottom <= sidebarBox.bottom) return;

    sidebar.scrollTop += activeBox.top - sidebarBox.top
      - (sidebarBox.height - activeBox.height) / 2;
  }

  var schedule = function () {
    repairGeneratedLayout();
    window.requestAnimationFrame(revealActiveBookItem);
  };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", schedule, { once: true });
  } else {
    schedule();
  }
}());
</script>
]])
end

-- Stable, server-rendered destinations include the controls as well as the plot.
function Div(el)
  if el.classes:includes("widget-frame") and el.identifier == "" then
    local number = (el.attributes["data-oznaka"] or ""):match("(%d+)%.%d+")
    if number then el.identifier = "interakcija-w" .. number end
    if number == "08" then
      el.content = pandoc.Blocks({
        pandoc.Div(el.content, pandoc.Attr("", {"widget-workbench"}))
      })
    end
    return el
  end
end

function Pandoc(doc)
  doc.blocks:insert(1, layout_script())
  return doc
end
