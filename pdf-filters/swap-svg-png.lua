-- Swaps SVG image sources to PNG for the PDF build.
--
-- The PDF engine cannot embed SVG without rsvg-convert on PATH (absent here).
-- Instead of dropping the infographics (the old strip-svg.lua workaround), we
-- pre-rasterize each SVG to a same-named .png (scripts/svg-to-png.R) and this
-- filter rewrites the image src from .svg to .png during the PDF render only.
-- The HTML build is untouched and keeps the crisp vector SVGs.
--
-- Pairs with: scripts/svg-to-png.R (regenerate PNGs when an SVG changes).

local function svg_to_png(src)
  if not src then return nil end
  -- rewrite a trailing ".svg" (optionally followed by ?query/#frag) to ".png"
  local new = src:gsub("%.svg(%f[^%w])", ".png%1")
  if new ~= src then return new end
  -- handle a plain trailing ".svg" with nothing after it
  if src:lower():match("%.svg$") then
    return src:sub(1, #src - 4) .. ".png"
  end
  return nil
end

function Image(img)
  local swapped = svg_to_png(img.src)
  if swapped then
    img.src = swapped
    return img
  end
  return nil
end
