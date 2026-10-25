-- U knjiznom PDF-u naslovnicu stvara tex/theme.tex. Web-only landing page
-- iz index.qmd ne smije otvoriti jos dva naslovna poglavlja.
function Pandoc(doc)
  if not (FORMAT:match("latex") or FORMAT:match("pdf")) then
    return nil
  end

  local blocks = pandoc.List({})
  local reached_preface = false
  local chapter_number = 0
  for _, block in ipairs(doc.blocks) do
    if block.t == "Header" and block.level == 1
      and pandoc.utils.stringify(block.content) == "Predgovor" then
      reached_preface = true
    end
    if reached_preface then
      if block.t == "Header" and block.level == 1 then
        local title = pandoc.utils.stringify(block.content)
        if title == "Predgovor" or title == "Literatura"
          or title == "Dodaci" or title:match("^DIO ")
          or title:match("^ZAVR") or chapter_number >= 18 then
          blocks:insert(pandoc.RawBlock("latex", "\\bklabeledfalse"))
        else
          chapter_number = chapter_number + 1
          blocks:insert(pandoc.RawBlock("latex",
            "\\bklabeledtrue\\renewcommand{\\bkchapterid}{"
              .. string.format("%02d", chapter_number) .. "}"))
        end
      end
      blocks:insert(block)
    end
  end
  if not reached_preface then
    error("PDF landing filter: Predgovor chapter not found")
  end
  if chapter_number ~= 18 then
    error("PDF landing filter: expected 18 numbered chapters, found " .. chapter_number)
  end
  doc.blocks = blocks
  return doc
end
