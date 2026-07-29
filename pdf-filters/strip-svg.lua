-- Drops SVG images from the document tree before PDF rendering.
--
-- The book's infographics (ch01/05/12/14) are authored as .svg. Converting
-- SVG to PDF requires `rsvg-convert` on the PATH, which is not always
-- available locally. Rather than fail the whole PDF build over four images,
-- this filter removes SVG images (and the figure/para that would be left
-- empty around them) so a complete, text-faithful PDF can be produced now.
-- The SVGs remain in the HTML build, which is unaffected by this filter.
--
-- TODO: once rsvg-convert (or a PNG fallback) is in place, remove this
-- filter from _quarto-pdf.yml so the infographics render in the PDF too.

local function is_svg(src)
  if not src then return false end
  -- match ".svg" optionally followed by a query/fragment, case-insensitive
  return src:lower():match("%.svg%f[^%w]") ~= nil
end

-- Remove a standalone SVG image. Returning {} deletes the inline element.
function Image(img)
  if is_svg(img.src) then
    return {}
  end
  return nil
end

-- A Quarto figure is typically a Para containing a single Image (plus an
-- optional caption). If that image is an SVG, drop the whole paragraph so
-- no empty figure shell or dangling caption is left behind.
function Para(para)
  if #para.content == 1 and para.content[1].t == "Image"
     and is_svg(para.content[1].src) then
    return {}
  end
  return nil
end

-- Quarto may also wrap figures in a Figure block (Pandoc >= 3). If its only
-- image is an SVG, remove the figure entirely.
function Figure(fig)
  local only_svg = true
  local saw_image = false
  fig.content:walk({
    Image = function(img)
      saw_image = true
      if not is_svg(img.src) then only_svg = false end
    end
  })
  if saw_image and only_svg then
    return {}
  end
  return nil
end
