# Unnumbered HTML previews for the online preface. Values are calculated from
# the same generated teaching datasets used by the chapters (R/setup.R).
# No sampling, new simulation or external empirical claim is introduced here.
local({
  number <- function(x, digits = 0) formatC(x, format = "f", digits = digits,
                                           decimal.mark = ",", big.mark = ".")
  coord <- function(x) formatC(x, format = "f", digits = 2, decimal.mark = ".")
  labels <- c("portal" = "Portali", "društvene mreže" = "Društvene mreže",
              "TV" = "Televizija", "radio" = "Radio", "tisak" = "Tisak")
  counts <- sort(table(populacija_medija$izvor_vijesti), decreasing = TRUE)
  stopifnot(setequal(names(counts), names(labels)), sum(counts) == nrow(populacija_medija))
  shares <- as.numeric(counts) / sum(counts)
  minutes <- anketa_mreze$minute_dnevno
  breaks <- seq(0, ceiling(max(minutes) / 30) * 30, by = 30)
  bins <- hist(minutes, breaks = breaks, right = FALSE, plot = FALSE)
  stopifnot(sum(bins$counts) == nrow(anketa_mreze), all(is.finite(minutes)))
  cat('<section class="preface-data preface-visual" aria-labelledby="preface-data-title">\n',
      '<p class="preface-eyebrow">Prvi susret s podacima</p>\n',
      '<p class="preface-visual-title" id="preface-data-title">Dvije simulacije, mnogo pitanja</p>\n',
      '<div class="preface-data-grid">\n',
      '<figure aria-labelledby="preface-city-title">\n',
      '<figcaption id="preface-city-title"><span class="preface-data-name">Zamišljeni grad</span>',
      '<span class="preface-data-count">', number(nrow(populacija_medija)), ' simuliranih osoba</span></figcaption>\n',
      '<p class="preface-data-question">Odakle dolaze njihove vijesti?</p>\n', sep = '')
  alt <- paste(paste(labels[names(counts)], paste0(number(100 * shares, 1), " %")), collapse = ", ")
  cat('<svg viewBox="0 0 270 190" role="img" aria-labelledby="preface-city-chart-title preface-city-chart-desc">',
      '<title id="preface-city-chart-title">Glavni izvor vijesti u simuliranoj populaciji</title>',
      '<desc id="preface-city-chart-desc">', alt, '. Svaka pozadinska traka predstavlja 100 % populacije.</desc>\n', sep = '')
  for (i in seq_along(counts)) {
    y <- (i - 1) * 37
    cat('<text class="preface-chart-label" x="0" y="', y + 12, '">', labels[names(counts)[i]], '</text>',
        '<text class="preface-chart-value" x="270" y="', y + 12, '" text-anchor="end">', number(100 * shares[i], 1), ' %</text>',
        '<rect class="preface-chart-track" x="0" y="', y + 20, '" width="270" height="7"/>',
        '<rect class="preface-chart-bar" x="0" y="', y + 20, '" width="', coord(270 * shares[i]), '" height="7"/>\n', sep = '')
  }
  cat('</svg>\n<p class="preface-data-note">Udjeli prema glavnom izvoru vijesti.</p>\n',
      '<a class="preface-text-link" href="../podaci.html#podaci-populacija-medija">Upoznajte grad <span aria-hidden="true">→</span></a>\n',
      '</figure>\n<figure aria-labelledby="preface-survey-title">\n',
      '<figcaption id="preface-survey-title"><span class="preface-data-name">Zasebna anketa</span>',
      '<span class="preface-data-count">', number(nrow(anketa_mreze)), ' simuliranih osoba</span></figcaption>\n',
      '<p class="preface-data-question">Koliko vremena provode na mrežama?</p>\n', sep = '')
  bin_labels <- paste0(head(breaks, -1), " do manje od ", tail(breaks, -1), " minuta")
  cat('<svg viewBox="0 0 270 190" role="img" aria-labelledby="preface-survey-chart-title preface-survey-chart-desc">',
      '<title id="preface-survey-chart-title">Dnevno vrijeme na društvenim mrežama u simuliranoj anketi</title>',
      '<desc id="preface-survey-chart-desc">Broj osoba po rasponu. ',
      paste(paste0(bin_labels, ", ", bins$counts, " osoba"), collapse = ". "), '.</desc>\n', sep = '')
  ymax <- ceiling(max(bins$counts) / 20) * 20
  xmax <- max(breaks)
  x <- function(v) 30 + v / xmax * 230
  y <- function(v) 155 - v / ymax * 124
  cat('<text class="preface-chart-label" x="30" y="13">Broj osoba</text>\n')
  for (tick in seq(0, ymax, by = 40)) {
    cat('<path class="preface-chart-grid" d="M30 ', coord(y(tick)), 'H260"/>',
        '<text class="preface-chart-value" x="23" y="', coord(y(tick) + 3), '" text-anchor="end">', tick, '</text>\n', sep = '')
  }
  for (i in seq_along(bins$counts)) {
    cat('<rect class="preface-chart-bar" x="', coord(x(breaks[i]) + 1), '" y="', coord(y(bins$counts[i])),
        '" width="', coord(230 / length(bins$counts) - 2), '" height="', coord(155 - y(bins$counts[i])), '">',
        '<title>', bin_labels[i], ', ', bins$counts[i], ' osoba</title></rect>\n', sep = '')
  }
  for (tick in seq(0, xmax, by = 60)) {
    cat('<text class="preface-chart-value" x="', coord(x(tick)), '" y="170" text-anchor="middle">', tick, '</text>\n', sep = '')
  }
  cat('<text class="preface-chart-label" x="260" y="188" text-anchor="end">Minute dnevno</text></svg>\n',
      '<p class="preface-data-note">Svaki stupac obuhvaća raspon od 30 minuta.</p>\n',
      '<a class="preface-text-link" href="../podaci.html#podaci-anketa-mreze">Upoznajte anketu <span aria-hidden="true">→</span></a>\n',
      '</figure>\n</div>\n',
      '<p class="preface-data-source">Izračun iz skupova <code>populacija_medija</code> i <code>anketa_mreze</code>. ',
      'Skupovi su generirani zasebno i opisuju zamišljene osobe.</p>\n</section>\n', sep = '')
})
