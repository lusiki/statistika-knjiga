"""
statistika_style.py — matplotlib style for the book's figures.

Mirrors knjiga-stil/R/theme_statistika.R exactly, so an R figure and a Python
figure on facing pages look like they came from one hand.

    from knjiga_stil.python.statistika_style import postavi_stil, PALETA, BOJE
    postavi_stil()                 # digital edition
    postavi_stil(tisak=True)       # black & white print block
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ── Boje ─────────────────────────────────────────────────────────────────────
BOJE = {
    "papir": "#FBFAF6",
    "papir_alt": "#F3EFE6",
    "ploha": "#FFFFFF",
    "tinta": "#16150F",
    "tekst": "#33322A",
    "prigusena": "#6E6C61",
    "slaba": "#9B9789",
    "linija": "#E4DFD2",
    "oker": "#C08A16",
    "oker_tekst": "#8A6212",
    "oker_ispun": "#FAF2DE",
}

# Poredano po svjetlini — preživljava pretvorbu u sivo
PALETA = ["#16150F", "#40566B", "#8A6212", "#9B9789", "#C9C2B0"]
PALETA_SEQ = ["#FAF2DE", "#E4C97E", "#C08A16", "#8A6212", "#4A3408"]
PALETA_DIV = ["#40566B", "#8FA0AE", "#EDE9DF", "#D9AE55", "#8A6212"]


def postavi_stil(tisak: bool = False, base_size: float = 10.0) -> None:
    """Apply the book style globally. Call once per notebook or script."""
    pozadina = "#FFFFFF" if tisak else BOJE["papir"]
    prigus = "#5A584F" if tisak else BOJE["prigusena"]
    slaba = "#8A887F" if tisak else BOJE["slaba"]
    linija = "#D8D8D8" if tisak else BOJE["linija"]

    mpl.rcParams.update({
        # tipografija
        "font.family": "Public Sans",
        "font.sans-serif": ["Public Sans", "DejaVu Sans"],
        "font.serif": ["Literata", "Georgia"],
        "font.monospace": ["JetBrains Mono", "DejaVu Sans Mono"],
        "font.size": base_size,
        "mathtext.fontset": "custom",
        "mathtext.rm": "Literata",
        "mathtext.it": "Literata:italic",

        # ploha
        "figure.facecolor": pozadina,
        "figure.edgecolor": "none",
        "axes.facecolor": pozadina,
        "savefig.facecolor": pozadina,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.06,
        "figure.figsize": (6.6, 4.0),
        "figure.dpi": 110,
        "savefig.dpi": 300,

        # osi: jedna crna linija na dnu, bez okvira
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.spines.left": False,
        "axes.spines.bottom": True,
        "axes.edgecolor": BOJE["tinta"],
        "axes.linewidth": 0.6,
        "axes.labelcolor": prigus,
        "axes.labelsize": base_size * 0.86,
        "axes.labelpad": 8,
        "axes.titlelocation": "left",
        "axes.titlesize": base_size * 1.5,
        "axes.titlecolor": BOJE["tinta"],
        "axes.titlepad": 12,
        "axes.titleweight": "normal",
        "axes.prop_cycle": mpl.cycler(color=PALETA),

        # mreža: vlas, samo vodoravna
        "axes.grid": True,
        "axes.grid.axis": "y",
        "grid.color": linija,
        "grid.linewidth": 0.45,
        "grid.alpha": 1.0,

        # kvačice: brojke u monospaceu, bez crtica
        "xtick.color": prigus,
        "ytick.color": prigus,
        "xtick.labelsize": base_size * 0.82,
        "ytick.labelsize": base_size * 0.82,
        "xtick.major.size": 0,
        "ytick.major.size": 0,
        "xtick.minor.size": 0,
        "ytick.minor.size": 0,
        "xtick.major.pad": 6,
        "ytick.major.pad": 6,

        # legenda: bez okvira, gore lijevo
        "legend.frameon": False,
        "legend.loc": "upper left",
        "legend.fontsize": base_size * 0.82,
        "legend.labelcolor": prigus,
        "legend.handlelength": 1.4,
        "legend.columnspacing": 1.6,

        # oznake
        "lines.linewidth": 1.5,
        "lines.markersize": 4.5,
        "patch.edgecolor": "none",
        "patch.facecolor": BOJE["oker"],
        "hatch.linewidth": 0.6,
        "text.color": BOJE["tekst"],
    })

    # brojke na osima u monospaceu
    for k in ("xtick.labelcolor", "ytick.labelcolor"):
        mpl.rcParams[k] = prigus

    global _SLABA
    _SLABA = slaba


_SLABA = BOJE["slaba"]


def mono_osi(ax) -> None:
    """Set tick labels in JetBrains Mono (matplotlib has no per-tick rcParam)."""
    for lbl in list(ax.get_xticklabels()) + list(ax.get_yticklabels()):
        lbl.set_fontfamily("JetBrains Mono")


def hr_format(decimala: int = 1) -> FuncFormatter:
    """Croatian axis numbers: decimal comma, space thousands separator."""
    def _f(x, _pos):
        s = f"{x:,.{decimala}f}"
        return s.replace(",", "\u00a0").replace(".", ",")
    return FuncFormatter(_f)


def naglasak(kategorije, istaknuto, boja: str = BOJE["oker"],
             ostalo: str = "#C9C2B0") -> list[str]:
    """One series in ochre, everything else muted."""
    return [boja if k == istaknuto else ostalo for k in kategorije]


def izvor(ax, tekst: str) -> None:
    """Source line under the plot, mono, faint — same as the R theme."""
    ax.annotate(tekst, xy=(0, 0), xycoords="axes fraction",
                xytext=(0, -46), textcoords="offset points",
                fontfamily="JetBrains Mono", fontsize=7.2,
                color=_SLABA, va="top", ha="left")


def spremi_figuru(fig, naziv: str, mapa: str = "slike") -> None:
    """Static twin of a widget: SVG for the web, PDF for print."""
    import os
    os.makedirs(mapa, exist_ok=True)
    fig.savefig(os.path.join(mapa, f"{naziv}.svg"))
    fig.savefig(os.path.join(mapa, f"{naziv}.pdf"))
