-- multiline-math-docx.lua
-- Pandoc's TeX->OMML (texmath) converter cannot parse a bare `\\` line break in
-- display math, so the book's few multi-line display equations authored as
-- `$$ ... \\[4pt] ... $$` fall back to raw TeX in Word. Wrapping them in an
-- `aligned` environment lets texmath convert them to native Word equations.
-- Only bare multi-line display math is touched (equations already inside an
-- environment carry a `\begin{` and are skipped). DOCX only; HTML/PDF untouched.

function Math(m)
  if not FORMAT:match("docx") then return nil end
  if m.mathtype == "DisplayMath"
     and m.text:find("\\\\", 1, true)
     and not m.text:find("\\begin{", 1, true) then
    -- texmath cannot parse the optional vertical-spacing form `\\[4pt]`; reduce
    -- it to a plain row break before wrapping the equation in `aligned`.
    local body = m.text:gsub("\\\\%s*%[[^%]]*%]", "\\\\")
    m.text = "\\begin{aligned}\n" .. body .. "\n\\end{aligned}"
    return m
  end
  return nil
end
