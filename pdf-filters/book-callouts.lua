-- book-callouts.lua
-- Quarto ne prepoznaje vlastite klase pedagoških kutija za LaTeX, pa bi u PDF-u
-- ispale kao obični pasusi. Ovaj filter svaku omata u tcolorbox okruženje
-- definirano u tex/theme.tex. Samo PDF.
--
-- Okruženja se razlikuju CRTOM I OZNAKOM, ne bojom: tiskani blok je crno-bijel
-- (vidi DESIGN.md, načelo 3).

local map = {
  ["callout-vinjeta"]  = "calloutvinjeta",
  ["callout-divljina"] = "calloutdivljina",
  ["callout-model"]    = "calloutmodel",
  ["callout-greska"]   = "calloutgreska",
  -- zatvarajući blok poglavlja
  ["primjer"]          = "calloutprimjer",
  ["sazetak"]          = "calloutsazetak",
}

function Div(el)
  if not (FORMAT:match("latex") or FORMAT:match("pdf")) then
    return nil
  end
  for _, cls in ipairs(el.classes) do
    local env = map[cls]
    if env then
      local out = pandoc.List({})
      out:insert(pandoc.RawBlock("latex", "\\begin{" .. env .. "}"))
      out:extend(el.content)
      out:insert(pandoc.RawBlock("latex", "\\end{" .. env .. "}"))
      return out
    end
  end
  return nil
end

-- Pojam s definicijom na dodir. U tisku nema oblačića: pojam ide u kurziv,
-- engleski termin uz vanjski rub.
--   [statističko zaključivanje]{.pojam def="…" en="statistical inference" ch="8"}
local function escape_tex(s)
  if not s then return nil end
  return (s:gsub("([&%%%$#_{}])", "\\%1"))
end

function Span(el)
  if not (FORMAT:match("latex") or FORMAT:match("pdf")) then
    return nil
  end
  if not el.classes:includes("pojam") then return nil end

  local out = pandoc.List({ pandoc.Emph(el.content) })
  local en = el.attributes["en"]
  if en then
    out:insert(pandoc.RawInline("latex", "\\marginnote{\\textit{" .. escape_tex(en) .. "}}"))
  end
  return out
end
