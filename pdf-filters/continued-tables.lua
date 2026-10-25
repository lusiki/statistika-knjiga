-- Run after Quarto has attached captions to generated LaTeX tables.
local function continued(text)
  if not text:find("\\begin{longtable}", 1, true) then return text end
  -- Quarto's caption Span becomes a TeX group when serialized separately;
  -- longtable requires the caption command at alignment level.
  text = text:gsub("{(\\caption%b{})}", "%1")
  if text:find("\\caption[]{(nastavak)}", 1, true) then return text end
  if text:find("\\endfirsthead", 1, true) then
    return text:gsub("(\\endfirsthead%s*)", "%1\\caption[]{(nastavak)}\\tabularnewline\n", 1)
  end
  local first, head, tail = text:match("^(.-)(\\toprule.-)\\endhead(.*)$")
  if first and first:find("\\caption", 1, true) then
    return first .. head .. "\\endfirsthead\n"
      .. "\\caption[]{(nastavak)}\\tabularnewline\n"
      .. head .. "\\endhead" .. tail
  end
  return text
end

local function print_table(text)
  -- A four-row table inside the breakable wild-statistics box must not
  -- install longtable's page-output routine inside tcolorbox. Keep this
  -- known short table atomic, with its caption and label intact.
  if text:find("\\label{tbl-kleppang}", 1, true) then
    local columns = text:match("\\begin{longtable}%[%](%b{})")
    local caption = text:match("\\caption(%b{})")
    local head = text:match("(\\toprule.-)\\endfirsthead")
      or text:match("(\\toprule.-)\\endhead")
    local body = text:match("\\endlastfoot%s*(.-)\\end{longtable}")
    assert(columns and caption and head and body,
      "The Kleppang print table structure changed; inspect its serializer.")
    return "\\par\\begin{minipage}{\\linewidth}\n\\captionof{table}"
      .. caption .. "\n\\begin{tabular}" .. columns .. "\n"
      .. head .. body .. "\n\\bottomrule\n\\end{tabular}\n"
      .. "\\end{minipage}\\par\\smallskip"
  end
  return continued(text)
end

function Table(el)
  if not FORMAT:match("latex") then return nil end
  return pandoc.RawBlock("latex", print_table(pandoc.write(pandoc.Pandoc({el}), "latex")))
end

function Blocks(blocks)
  if not FORMAT:match("latex") then return nil end
  local result, pending = pandoc.List(), nil
  for _, block in ipairs(blocks) do
    if block.t == "RawBlock" and block.text:find("\\label{tbl-kleppang}", 1, true)
      and #result > 0 and result[#result].t == "RawBlock"
      and result[#result].text:match("^%s*\\Needspace%b{}%s*$") then
      -- The atomic minipage supplies its own size to the breakable box.
      -- Needspace consults the outer page and prematurely splits this box.
      table.remove(result, #result)
    end
    if block.t == "RawBlock" and block.text:find("\\begin{longtable}", 1, true) then
      pending = pandoc.List()
    end
    if pending then
      pending:insert(block)
      if block.t == "RawBlock" and block.text:find("\\end{longtable}", 1, true) then
        local latex = pandoc.write(pandoc.Pandoc(pending), "latex")
        if latex:find("\\label{tbl-kleppang}", 1, true)
          and #result > 0 and result[#result].t == "RawBlock"
          and result[#result].text:match("^%s*\\Needspace%b{}%s*$") then
          table.remove(result, #result)
        end
        result:insert(pandoc.RawBlock("latex", print_table(latex)))
        pending = nil
      end
    else
      result:insert(block)
    end
  end
  if pending then result:extend(pending) end
  return result
end

return {
  {Pandoc = function(doc)
    if FORMAT:match("latex") then
      local cited = pandoc.utils.citeproc(doc)
      -- A question mark immediately before a Croatian closing quote can
      -- become TeX's ?` ligature. Preserve the punctuation in cited titles.
      return cited:walk({Str = function(el)
        if not el.text:find("?", 1, true) then return nil end
        local result, start = pandoc.Inlines({}), 1
        while true do
          local at = el.text:find("?", start, true)
          if not at then
            if start <= #el.text then result:insert(pandoc.Str(el.text:sub(start))) end
            break
          end
          if at > start then result:insert(pandoc.Str(el.text:sub(start, at - 1))) end
          result:insert(pandoc.RawInline("latex", "?{}"))
          start = at + 1
        end
        return result
      end})
    end
  end},
  {Table = Table, Blocks = Blocks}
}
