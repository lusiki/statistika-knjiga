# Statična ilustracija za poglavlje 5. Ulaz se preuzima zasebno, nikad pri renderu.
# Izvor, prikvačena inačica i licenca: images/datasaurus/PROVENANCE.md.
args <- commandArgs(trailingOnly = TRUE)
options(error = function() { traceback(3); quit(status = 1) })
stopifnot(length(args) == 1L, file.exists(args[[1]]))
stopifnot(unname(tools::md5sum(args[[1]])) == "c71ae2ac4233aa73d43691f24158b9c6")
source("R/setup.R")
d <- read.delim(args[[1]], stringsAsFactors = FALSE)
d <- d[d$dataset %in% c("dino", "circle"), ]
stopifnot(nrow(d) == 284L, all(table(d$dataset) == 142L))
d$skup <- factor(d$dataset, levels = c("dino", "circle"),
                 labels = c("Skup A", "Skup B"))
print(aggregate(cbind(x, y) ~ skup, d, mean))
print(aggregate(cbind(x, y) ~ skup, d, sd))
stopifnot(all(round(aggregate(cbind(x, y) ~ skup, d, mean)$x, 1) == 54.3),
          all(round(aggregate(cbind(x, y) ~ skup, d, mean)$y, 1) == 47.8),
          all(round(aggregate(cbind(x, y) ~ skup, d, sd)$x, 1) == 16.8),
          all(round(aggregate(cbind(x, y) ~ skup, d, sd)$y, 1) == 26.9))
p <- ggplot(d, aes(x, y)) +
  geom_point(size = 1.3, colour = boje_knjige[[1]]) +
  facet_wrap(~ skup, nrow = 1) +
  coord_equal(xlim = c(0, 100), ylim = c(0, 100)) +
  labs(x = "x", y = "y") +
  theme_knjiga(base_size = 13, mreza = "oboje")
dir.create("images/datasaurus", recursive = TRUE, showWarnings = FALSE)
ggsave("images/datasaurus/reveal-light.svg", p, width = 6.6, height = 3.5, bg = "transparent")
ggsave("images/datasaurus/reveal-print.pdf", p, width = 6.6, height = 3.5,
       device = cairo_pdf, bg = "white")
pd <- p + theme_knjiga(base_size = 13, mreza = "oboje", varijanta = "tamna")
pd$layers[[1]]$aes_params$colour <- boje_knjige_tamne[[1]]
ggsave("images/datasaurus/reveal-dark.svg", pd, width = 6.6, height = 3.5, bg = "transparent")
