# Convert the book's infographic SVGs to high-res PNG for the PDF build.
#
# The PDF cannot embed SVG without rsvg-convert on PATH (absent here). Rather
# than strip the infographics (the old strip-svg.lua workaround), we rasterize
# them with the rsvg R package (bundles librsvg) and point the PDF at the PNGs.
#
# Run: Rscript scripts/svg-to-png.R   (renv activated via this script)

source("renv/activate.R")
library(rsvg)

dir <- "images/infographics"
svgs <- list.files(dir, pattern = "\\.svg$", full.names = TRUE)

for (s in svgs) {
  out <- sub("\\.svg$", ".png", s)
  rsvg::rsvg_png(s, out, width = 2400)  # 3x the 800px viewBox -> crisp in print
  kb <- round(file.info(out)$size / 1024, 1)
  cat(sprintf("%-44s %s KB\n", basename(out), kb))
}
