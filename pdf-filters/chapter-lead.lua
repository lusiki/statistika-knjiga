-- chapter-lead.lua
-- Sustav Zvono, tisak. Quarto podnaslov poglavlja (YAML subtitle) ispisuje kao
-- odlomak iza naslova razine 1, praćen blokom sa samim prijelomom retka
-- (\hfill\break). Taj se par zamjenjuje okruženjem bkchapterlead iz
-- tex/theme.tex: Literata kurziv, pa crta od 1,2 pt koja zatvara otvaranje.
--
-- Podnaslov Quarto umeće kasno, pa filtar radi na točki post-render
-- (_quarto-pdf.yml). Između naslova i podnaslova smiju stajati samo sirovi
-- LaTeX blokovi (\label, \Needspace). Poglavlja bez podnaslova ostaju netaknuta.

local function only_linebreaks(block)
  if block and block.t == "RawBlock" then
    return block.text:match("^%s*\\hfill\\break%s*$") ~= nil
  end
  if not block or (block.t ~= "Para" and block.t ~= "Plain") or #block.content == 0 then
    return false
  end
  for _, inline in ipairs(block.content) do
    if inline.t ~= "LineBreak" and inline.t ~= "Space" and inline.t ~= "SoftBreak" then
      return false
    end
  end
  return true
end

function Blocks(blocks)
  if not (FORMAT:match("latex") or FORMAT:match("pdf")) then
    return nil
  end
  local out = pandoc.List({})
  local changed = false
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    out:insert(b)
    i = i + 1
    if b.t == "Header" and b.level == 1 then
      local j = i
      while j <= #blocks and blocks[j].t == "RawBlock"
        and not only_linebreaks(blocks[j]) do
        j = j + 1
      end
      local nxt = blocks[j]
      if nxt and nxt.t == "Para" and only_linebreaks(blocks[j + 1]) then
        for k = i, j - 1 do out:insert(blocks[k]) end
        out:insert(pandoc.RawBlock("latex", "\\begin{bkchapterlead}"))
        out:insert(nxt)
        out:insert(pandoc.RawBlock("latex", "\\end{bkchapterlead}"))
        changed = true
        i = j + 2
      end
    end
  end
  if changed then return out end
  return nil
end
