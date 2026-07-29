-- book-callouts.lua
-- Quarto ne prepoznaje vlastite klase pedagoških kutija za LaTeX, pa bi u PDF-u
-- ispale kao obični pasusi. Ovaj filter svaku omata u tcolorbox okruženje
-- definirano u tex/theme.tex. Samo PDF.

local map = {
  ["callout-vinjeta"]  = "calloutvinjeta",
  ["callout-divljina"] = "calloutdivljina",
  ["callout-model"]    = "calloutmodel",
  ["callout-greska"]   = "calloutgreska",
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
