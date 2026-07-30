-- Turn each chapter's compact bilingual terms paragraph into a semantic list.
--
-- Authors keep the deliberately light source form
--
--   hrvatski pojam (*English term*), drugi pojam (*second term*)
--
-- while HTML receives a definition list whose term and description form a
-- readable two-column row.  The filter fails closed: if a terms paragraph does
-- not match the expected Croatian + emphasized-English pairs, it is left
-- untouched instead of losing content.

local function has_class(element, class_name)
  for _, value in ipairs(element.classes or {}) do
    if value == class_name then
      return true
    end
  end
  return false
end

local function is_spacing(inline)
  return inline.t == "Space"
    or inline.t == "SoftBreak"
    or inline.t == "LineBreak"
end

local function is_separator(inline)
  return is_spacing(inline)
    or (inline.t == "Str" and inline.text:match("^[,()]+$") ~= nil)
end

local function trim_croatian(inlines)
  local first = 1
  local last = #inlines

  while first <= last and is_separator(inlines[first]) do
    first = first + 1
  end

  while last >= first and is_spacing(inlines[last]) do
    last = last - 1
  end

  -- The source writes the English translation as `(*English*)`, so Pandoc
  -- places the opening parenthesis immediately before the Emph node.
  if last >= first
    and inlines[last].t == "Str"
    and inlines[last].text == "(" then
    last = last - 1
  end

  while last >= first and is_spacing(inlines[last]) do
    last = last - 1
  end

  local trimmed = pandoc.List()
  for index = first, last do
    trimmed:insert(inlines[index])
  end
  return trimmed
end

local function only_separators_remain(inlines)
  for _, inline in ipairs(inlines) do
    if not is_separator(inline) then
      return false
    end
  end
  return true
end

local function parse_pairs(inlines)
  local pairs = {}
  local croatian = pandoc.List()

  for _, inline in ipairs(inlines) do
    if inline.t == "Emph" then
      local term = trim_croatian(croatian)
      if #term == 0 or #inline.content == 0 then
        return nil
      end

      table.insert(pairs, {
        croatian = term,
        english = inline.content
      })
      croatian = pandoc.List()
    else
      croatian:insert(inline)
    end
  end

  if #pairs == 0 or not only_separators_remain(croatian) then
    return nil
  end
  return pairs
end

local function terminology_list(paragraph)
  local pairs = parse_pairs(paragraph.content)
  if not pairs then
    return nil
  end

  local items = {}
  for _, pair in ipairs(pairs) do
    local croatian = pandoc.Span(
      pair.croatian,
      pandoc.Attr("", { "terminology-list__hr" }, { { "lang", "hr" } })
    )
    local english = pandoc.Span(
      pair.english,
      pandoc.Attr("", { "terminology-list__en" }, { { "lang", "en" } })
    )

    table.insert(items, {
      { croatian },
      { { pandoc.Plain({ english }) } }
    })
  end

  return pandoc.Div(
    { pandoc.DefinitionList(items) },
    pandoc.Attr("", { "terminology-list" })
  )
end

function Blocks(input)
  local blocks = pandoc.List()
  local next_paragraph_is_terms = false

  for _, block in ipairs(input) do
    if block.t == "Header"
      and block.level == 2
      and has_class(block, "pojmovi") then
      next_paragraph_is_terms = true
      blocks:insert(block)
    elseif next_paragraph_is_terms and block.t == "Para" then
      blocks:insert(terminology_list(block) or block)
      next_paragraph_is_terms = false
    else
      blocks:insert(block)
      if block.t ~= "RawBlock" then
        next_paragraph_is_terms = false
      end
    end
  end

  return blocks
end
