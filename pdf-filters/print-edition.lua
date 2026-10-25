-- Print edition: omit appendices before Quarto builds cross-references/TOC,
-- and retain definition prose without theorem-style labels or numbering.
local function is_print()
  return FORMAT:match("latex") or FORMAT:match("pdf")
end

local printed_routes = {}
local chapter_titles = {}
local current_chapter = nil
do
  local source = assert(io.open("assessment/print-navigation.json", "r"))
  chapter_titles = pandoc.json.decode(source:read("*a"))
  source:close()
end
local data_routes = nil

local function canonical_site()
  local config = assert(io.open("_quarto.yml", "r"))
  local source = config:read("*a")
  config:close()
  return assert(source:match('site%-url:%s*"([^"]+)"'),
    "Print links require the canonical site-url"):gsub("/$", "")
end

local function public_data_route(path)
  if not data_routes then
    local source = assert(io.open("config/appendix-c-data-route.json", "r"))
    local routes = pandoc.json.decode(source:read("*a"))
    source:close()
    data_routes = {}
    for _, package in ipairs(routes.package_routes) do
      if type(package.declared_files) == "table" then
        for _, file in ipairs(package.declared_files) do
          data_routes[file] = true
        end
      end
    end
  end
  return data_routes[path]
end

local function with_printed_address(link)
  if not printed_routes[link.target] then
    printed_routes[link.target] = true
    local target = link.target:gsub("([%%#])", "\\%1")
    local address = "\\url{" .. target .. "}"
    local base, file = target:match("^(.-/)([^/]+%.html)$")
    if base and #file < 42 then
      address = "\\href{" .. target .. "}{\\nolinkurl{" .. base .. "}\\nobreak\\mbox{\\nolinkurl{" .. file .. "}}}"
    end
    return pandoc.Inlines({link, pandoc.Note({pandoc.Para({
      pandoc.RawInline("latex", address)
    })})})
  end
  return link
end

function Pandoc(doc)
  if not is_print() then return nil end
  local kept = pandoc.List()
  for _, block in ipairs(doc.blocks) do
    -- Quarto may already have lowered the synthetic appendix heading to
    -- a LaTeX part command by this stage. Also inspect nested headings.
    local appendix = false
    local function raw(el)
      if el.text:find("\\appendix", 1, true) then appendix = true end
    end
    local function heading(el)
      local title = pandoc.utils.stringify(el.content)
      if el.level == 1 and (title == "Dodaci" or title == "Appendices") then
        appendix = true
      end
    end
    if block.t == "Header" then heading(block) end
    if block.t == "RawBlock" then raw(block) end
    block:walk({
      Header = heading,
      RawInline = raw,
      RawBlock = raw
    })
    if appendix then break end
    kept:insert(block)
  end
  doc.blocks = kept
  return doc
end

function Div(el)
  if not is_print() then return nil end
  if el.identifier:match("^def%-") then
    el.identifier = el.identifier:gsub("^def%-", "pojam-")
    el.classes:insert("print-definition")
    return el
  end
end

-- Quarto parses theorem divs into its extended AST before pre-quarto filters.
-- Unwrap that node too; changing only a nested Div cannot change its label.
function Theorem(el)
  if not is_print() or not el.identifier:match("^def%-") then return nil end
  local body = el.div
  if body.t ~= "Div" then body = pandoc.Div(body) end
  body.identifier = el.identifier:gsub("^def%-", "pojam-")
  body.classes:insert("print-definition")
  return body
end

function Header(el)
  if not is_print() then return nil end
  local title = pandoc.utils.stringify(el.content)
  if chapter_titles[title] and el.level == 1 then
    current_chapter = chapter_titles[title]
    return {el, pandoc.RawBlock("latex", "\\label{audit-ch" .. current_chapter .. "}")}
  end
  if title == "Pojmovi" and current_chapter then
    return {el, pandoc.RawBlock("latex", "\\label{audit-terms" .. current_chapter .. "}")}
  end
  if title == "Literatura" then
    local source = assert(io.open("assessment/print-checks.md", "r"),
      "Generate assessment/print-checks.md through build-solution-routes.py")
    local markdown = source:read("*a")
    source:close()
    local blocks = pandoc.List()
    local apparatus = assert(io.open("assessment/print-glossary.md", "r"))
    local glossary = apparatus:read("*a")
    apparatus:close()
    for _, block in ipairs(pandoc.read(glossary, "markdown").blocks) do
      if block.t == "Table" and #block.colspecs == 2
        and #block.head.rows > 0
        and pandoc.utils.stringify(block.head.rows[1].cells[1].contents) == "Oznaka" then
        block.colspecs = {{"AlignLeft", 0.25}, {"AlignLeft", 0.75}}
      end
      if block.t == "Header" and block.level == 2 then
        blocks:insert(pandoc.RawBlock("latex", "\\phantomsection"))
      end
      blocks:insert(block:walk({Str = Str, Math = Math, Inlines = Inlines}))
    end
    for _, block in ipairs(pandoc.read(markdown, "markdown").blocks) do
      if block.t == "Header" and block.level == 2 then
        blocks:insert(pandoc.RawBlock("latex", "\\phantomsection"))
      end
      blocks:insert(block:walk({Str = Str, Math = Math, Inlines = Inlines}))
    end
    blocks:insert(el)
    return blocks
  end
  if title:match("^Interakcija — ") then
    el.content = pandoc.Inlines(title:gsub("^Interakcija — ", ""))
    return el
  end
end

-- Let long file paths wrap at punctuation instead of crossing the trim edge.
function CodeBlock(el)
  if not is_print() then return nil end
  local lines = {}
  for line in (el.text .. "\n"):gmatch("([^\n]*)\n") do
    if #line > 60 then
      line = line:gsub(" |>%s*", " |>\n  ")
    end
    table.insert(lines, line)
  end
  el.text = table.concat(lines, "\n")
  if #lines <= 15 then
    return {pandoc.RawBlock("latex", "\\Needspace{" .. (#lines + 2) .. "\\baselineskip}"), el}
  end
  return el
end

function Code(el)
  if not is_print() then return nil end
  if el.text:match("^data/") and public_data_route(el.text) then
    return with_printed_address(pandoc.Link(
      {pandoc.RawInline("latex", "\\nolinkurl{" .. el.text .. "}")},
      canonical_site() .. "/" .. el.text))
  end
  if el.text:find("/", 1, true) and el.text:match("^[%w_./%-]+%.[%w]+$") then
    return pandoc.RawInline("latex", "\\nolinkurl{" .. el.text .. "}")
  end
end

function Link(el)
  if not is_print() then return nil end
  local relative = el.target:gsub("^%.%./", "")
  local online = relative:match("^dodaci/.+")
    or relative:match("^rjesenja%.qmd.*")
    or relative:match("^podaci%.qmd.*")
    or relative:match("^interakcije%.qmd.*")
  if online then
    el.target = canonical_site() .. "/" .. relative:gsub("%.qmd", ".html")
    local label = pandoc.utils.stringify(el.content)
    if label:match("^Dodatak") then
      el.content = pandoc.Inlines("Mrežni " .. label:gsub("^Dodatak", "dodatak"))
    end
    -- Numerical reminders sit in margin notes, which cannot contain footnotes.
    -- Their paper-access address is given in the preface.
    if relative:match("^dodaci/g%-numericki%-podsjetnik%.qmd#") then return el end
    return with_printed_address(el)
  end
end

-- Decimal comma spacing and a typographic minus affect prose/math, never code.
function Math(el)
  if not is_print() then return nil end
  el.text = el.text:gsub("(%d),(%d)", "%1{,}%2")
  return el
end

function Str(el)
  if not is_print() then return nil end
  el.text = el.text:gsub("^%-(%d)", "−%1")
  el.text = el.text:gsub("([%[%(;])%-(%d)", "%1−%2")
  if el.text:match("^%d[%d%./]*%.%d%d%d[%d%./,;:]*$" ) then
    local ending = el.text:match("([,;:%.])$") or ""
    local number = ending == "" and el.text or el.text:sub(1, -2)
    el.text = number:gsub("%.(%d%d%d)", " %1") .. ending
  end
  return el
end

function Table(el)
  if not is_print() then return nil end
  -- This short boxed table is made atomic by the late table filter.
  -- Needspace inside tcolorbox consults the wrong outer-page height.
  if el.identifier == "tbl-kleppang"
    or pandoc.utils.stringify(el):lower():find("kleppang", 1, true) then
    return nil
  end
  local rows = #el.head.rows + #el.foot.rows
  for _, body in ipairs(el.bodies) do rows = rows + #body.head + #body.body end
  if rows > 0 and rows <= 16 then
    local chars = #pandoc.utils.stringify(el)
    local lines = math.min(38, math.max(7 + rows * 2, 7 + math.ceil(chars / 45)))
    return {pandoc.RawBlock("latex", "\\Needspace{" .. lines .. "\\baselineskip}"), el}
  end
end

function Inlines(items)
  if not is_print() then return nil end
  for i = 2, #items - 1 do
    if items[i].t == "Space" and items[i - 1].t == "Str"
      and items[i + 1].t == "Str" and items[i - 1].text:match("%d$")
      and (items[i + 1].text:match("^%%")
        or items[i + 1].text:match("^%d%d%d[,;:%.]?$")) then
      items[i] = pandoc.Str(" ")
    end
  end
  return items
end
