-- book-callouts-docx.lua
-- Pedagoške kutije knjige (.callout-vinjeta/divljina/model/greska) su CSS-om
-- stilizirani divovi, ne izvorni Quarto callouti. U DOCX-u ih Quarto svede na
-- goli sadržaj i čitatelj izgubi oznaku kategorije. Ovaj filter dodaje podebljani
-- natpis i omata kutiju u blok citat da ostane vizualno odvojena u Wordu.
-- Samo DOCX (zrcali pdf-filters/book-callouts.lua).

local labels = {
  ["callout-vinjeta"]  = "Vinjeta",
  ["callout-divljina"] = "Statistika u divljini",
  ["callout-model"]    = "Pitajte model",
  ["callout-greska"]   = "Nađite grešku",
}

function Div(el)
  if not FORMAT:match("docx") then
    return nil
  end
  for _, cls in ipairs(el.classes) do
    local label = labels[cls]
    if label then
      local heading = pandoc.Para({ pandoc.Strong(pandoc.Str(label)) })
      local out = pandoc.List({ heading })
      out:extend(el.content)
      return pandoc.BlockQuote(out)
    end
  end
  return nil
end
