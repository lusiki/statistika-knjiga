--[[
  statistika.lua — element repertoire for "Osnove statistike za društvene znanosti"

  Turns plain Quarto fenced divs into the book's styled elements, in HTML and in
  print, from one source. Croatian class names, so chapter source reads as prose.

      ::: {.vinjeta}
      U studenome 2024. agencija je objavila…
      :::

      ::: {.definicija term="Distribucija uzorkovanja" en="sampling distribution"}
      Distribucija neke statistike preko svih mogućih uzoraka…
      :::

      ::: {.divljina claim="Podrška je porasla za 3 boda." source="portal, 2025"}
      Margina pogreške odnosi se na jednu procjenu, ne na razliku dviju…
      :::

      ::: {.pitajte prompt="Objasni razliku između SD i SE na mojim podacima."}
      Asistent dobro objašnjava… **Provjerite:** je li n isti.
      :::

      ::: {.pogreska}
      Interval pouzdanosti od 95 % ne znači…
      :::

      ::: {.sazetak}
      - Jedan uzorak daje jednu procjenu.
      :::

      ::: {.primjer}
      ### Pitanje
      ### Podaci
      ### Model
      :::

      ::: {.widget id="08.1" title="Stroj za CLT" fig="8.4" static="slike/08-clt.svg"}
      ```{ojs}
      …
      ```
      :::

      ::: {.zadaci}
      ### Pojmovno
      1. …
      ### Računski
      ### Kritički
      ### Revizija modela
      :::

      ::: {.pojmovi}
      | distribucija uzorkovanja | sampling distribution |
      :::

  Inline glossary term:  [statističko zaključivanje]{.pojam en="statistical inference" def="Izvođenje tvrdnji o populaciji na temelju uzorka." ch="8"}
--]]

local LABELS = {
  vinjeta    = "Vinjeta",
  definicija = "Definicija",
  divljina   = "Statistika u divljini",
  pitajte    = "Pitajte model",
  pogreska   = "Česta pogreška",
  primjer    = "Razrađeni primjer",
  sazetak    = "Sažetak",
  zadaci     = "Zadaci",
  pojmovi    = "Pojmovi",
}

local function html() return quarto.doc.is_format("html") end
local function attr(el, k) return el.attributes[k] end

local function raw(s) return pandoc.RawBlock(html() and "html" or "latex", s) end

-- ── HTML builders ───────────────────────────────────────────────────────────
local function h_open(cls, label, labelcls)
  local s = '<div class="' .. cls .. '">'
  if label then s = s .. '<div class="' .. (labelcls or cls .. '__label') .. '">' .. label .. '</div>' end
  return pandoc.RawBlock("html", s)
end
local function h_close() return pandoc.RawBlock("html", "</div>") end

-- ── LaTeX builders (print) ──────────────────────────────────────────────────
-- Environments are defined in knjiga-stil/tisak/preamble.tex
local function l_open(env, arg)
  return pandoc.RawBlock("latex", "\\begin{" .. env .. "}" .. (arg and ("{" .. arg .. "}") or ""))
end
local function l_close(env) return pandoc.RawBlock("latex", "\\end{" .. env .. "}") end

local function escape_tex(s)
  if not s then return nil end
  return s:gsub("([&%%%$#_{}])", "\\%1")
end

-- ── Element handlers ────────────────────────────────────────────────────────
local H = {}

H.vinjeta = function(el)
  if html() then
    local b = { h_open("st-vignette", LABELS.vinjeta) }
    for _, x in ipairs(el.content) do b[#b + 1] = x end
    b[#b + 1] = h_close()
    return b
  end
  local b = { l_open("stvinjeta") }
  for _, x in ipairs(el.content) do b[#b + 1] = x end
  b[#b + 1] = l_close("stvinjeta")
  return b
end

H.definicija = function(el)
  local term, en = attr(el, "term"), attr(el, "en")
  if html() then
    local b = { h_open("st-def", LABELS.definicija) }
    if term then b[#b + 1] = pandoc.RawBlock("html", '<div class="st-def__term">' .. term .. "</div>") end
    for _, x in ipairs(el.content) do b[#b + 1] = x end
    if en then b[#b + 1] = pandoc.RawBlock("html", '<div class="st-def__en">' .. en .. "</div>") end
    b[#b + 1] = h_close()
    return b
  end
  local b = { l_open("stdefinicija", escape_tex(term) or "") }
  for _, x in ipairs(el.content) do b[#b + 1] = x end
  if en then b[#b + 1] = pandoc.RawBlock("latex", "\\stdefen{" .. escape_tex(en) .. "}") end
  b[#b + 1] = l_close("stdefinicija")
  return b
end

H.divljina = function(el)
  local claim, src = attr(el, "claim"), attr(el, "source")
  if html() then
    local b = { h_open("st-wild", LABELS.divljina) }
    if claim then b[#b + 1] = pandoc.RawBlock("html", '<div class="st-wild__claim">„' .. claim .. "”</div>") end
    for _, x in ipairs(el.content) do b[#b + 1] = x end
    if src then b[#b + 1] = pandoc.RawBlock("html", '<div class="st-wild__src">Izvor: ' .. src .. "</div>") end
    b[#b + 1] = h_close()
    return b
  end
  local b = { l_open("stdivljina", escape_tex(claim) or "") }
  for _, x in ipairs(el.content) do b[#b + 1] = x end
  if src then b[#b + 1] = pandoc.RawBlock("latex", "\\stsource{Izvor: " .. escape_tex(src) .. "}") end
  b[#b + 1] = l_close("stdivljina")
  return b
end

H.pitajte = function(el)
  local prompt = attr(el, "prompt")
  if html() then
    local b = { h_open("st-ask", LABELS.pitajte) }
    for _, x in ipairs(el.content) do b[#b + 1] = x end
    if prompt then b[#b + 1] = pandoc.RawBlock("html", '<div class="st-ask__prompt">&gt; ' .. prompt .. "</div>") end
    b[#b + 1] = h_close()
    return b
  end
  local b = { l_open("stpitajte") }
  for _, x in ipairs(el.content) do b[#b + 1] = x end
  if prompt then b[#b + 1] = pandoc.RawBlock("latex", "\\stprompt{" .. escape_tex(prompt) .. "}") end
  b[#b + 1] = l_close("stpitajte")
  return b
end

local function simple(cls, env, label, labelcls)
  return function(el)
    if html() then
      local b = { h_open(cls, label, labelcls) }
      for _, x in ipairs(el.content) do b[#b + 1] = x end
      b[#b + 1] = h_close()
      return b
    end
    local b = { l_open(env) }
    for _, x in ipairs(el.content) do b[#b + 1] = x end
    b[#b + 1] = l_close(env)
    return b
  end
end

H.pogreska = simple("st-warn", "stpogreska", LABELS.pogreska)
H.sazetak  = simple("st-summary", "stsazetak", LABELS.sazetak, "st-summary__label")
H.primjer  = simple("st-worked", "stprimjer", LABELS.primjer, "st-worked__label")
H.zadaci   = simple("st-ex", "stzadaci", nil)
H.pojmovi  = simple("st-glossary", "stpojmovi", nil)

H.widget = function(el)
  local id    = attr(el, "id") or ""
  local title = attr(el, "title") or "Interaktivni prikaz"
  local fig   = attr(el, "fig")
  local stat  = attr(el, "static")

  if html() then
    local b = {}
    b[#b + 1] = pandoc.RawBlock("html",
      '<div class="st-widget" id="widget-' .. id:gsub("%.", "-") .. '">' ..
      '<div class="st-widget__head"><h3 class="st-widget__title">' .. title .. "</h3>" ..
      '<div class="st-widget__tag">Widget ' .. id .. " · interaktivno</div></div>" ..
      '<div class="st-widget__body">')
    for _, x in ipairs(el.content) do b[#b + 1] = x end
    b[#b + 1] = pandoc.RawBlock("html", "</div>" ..
      (fig and ('<div class="st-widget__foot"><span>U tisku: statična figura.</span><span>Slika ' .. fig .. "</span></div>") or "") ..
      "</div>")
    return b
  end

  -- Print: the widget is replaced by its static twin. OJS/observable is dropped.
  if stat then
    local cap = title .. (fig and "" or "")
    return {
      pandoc.RawBlock("latex", "\\begin{figure}[htbp]\\centering"),
      pandoc.Para({ pandoc.Image({ pandoc.Str(cap) }, stat, cap) }),
      pandoc.RawBlock("latex", "\\end{figure}"),
    }
  end
  return {}
end

-- ── Dispatch ────────────────────────────────────────────────────────────────
function Div(el)
  for cls, fn in pairs(H) do
    if el.classes:includes(cls) then return fn(el) end
  end
  -- Drop screen-only / print-only blocks
  if el.classes:includes("samo-zaslon") and not html() then return {} end
  if el.classes:includes("samo-tisak") and html() then return {} end
  return nil
end

-- Inline glossary term
function Span(el)
  if not el.classes:includes("pojam") then return nil end
  local def, en, ch = el.attributes["def"], el.attributes["en"], el.attributes["ch"]
  if html() then
    local text = pandoc.utils.stringify(el.content)
    local tip = '<span class="st-term__tip"><span class="st-term__head">' .. text .. "</span>" ..
                (def or "") ..
                (en and (' <em class="st-term__en">' .. en .. "</em>") or "") ..
                (ch and (' <span class="st-term__ch">→ pogl. ' .. ch .. "</span>") or "") .. "</span>"
    return pandoc.RawInline("html", '<span class="st-term" tabindex="0">' .. text .. tip .. "</span>")
  end
  -- Print: term in italics, English in the margin
  local out = { pandoc.Emph(el.content) }
  if en then out[#out + 1] = pandoc.RawInline("latex", "\\marginnote{\\textit{" .. escape_tex(en) .. "}}") end
  return out
end

-- Strip OJS cells entirely from print output (their static twins carry them)
function CodeBlock(el)
  if not html() and (el.classes:includes("cell-code") or el.classes:includes("ojs")) then return {} end
  return nil
end

return {
  { Div = Div, Span = Span, CodeBlock = CodeBlock }
}
