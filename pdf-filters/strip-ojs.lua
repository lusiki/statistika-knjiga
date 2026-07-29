-- Strips OJS code blocks from the document tree before PDF rendering.
-- OJS chunks are HTML-only; in PDF they would either error or produce
-- empty output that disrupts the surrounding prose. Quarto already skips
-- them in most cases, but this filter is a guaranteed safety net.

function CodeBlock(block)
  for _, cls in ipairs(block.classes) do
    if cls == "ojs" or cls == "{ojs}" then
      return {}
    end
  end
  return nil
end

-- Quarto wraps cells in Div elements with class "cell" and language-specific
-- subclasses. Catch any cell whose content is OJS as a second safety net.
function Div(div)
  if div.classes:includes("cell") then
    for _, cls in ipairs(div.classes) do
      if cls == "cell-ojs" or cls:match("ojs") then
        return {}
      end
    end
  end
  return nil
end
