-- Tiskani metapodatci poglavlja imaju dva stupca: kratku oznaku i punu vrijednost.
-- Web i dalje koristi izvornu tablicu u chapter-meta divu.
local function escape_tex(s)
  return (s:gsub("([&%%%$#_{}])", "\\%1"))
end

function Div(el)
  if not (FORMAT:match("latex") or FORMAT:match("pdf")) then return nil end
  if not el.classes:includes("chapter-meta") then return nil end
  local tbl = el.content[1]
  if not tbl or tbl.t ~= "Table" or #tbl.bodies ~= 1
    or #tbl.bodies[1].body ~= 1 then
    error("PDF chapter-meta: expected one four-column table")
  end
  local cells = tbl.bodies[1].body[1].cells
  if #cells ~= 4 then
    error("PDF chapter-meta: expected four values")
  end
  local values = {}
  for _, cell in ipairs(cells) do
    values[#values + 1] = "{" .. escape_tex(pandoc.utils.stringify(cell.contents)) .. "}"
  end
  return pandoc.RawBlock("latex", "\\bkchaptermeta" .. table.concat(values))
end
