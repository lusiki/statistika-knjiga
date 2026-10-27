# Datasaurus — ilustracija u petom poglavlju

Statične figure nacrtali su autori knjige iz skupova `dino` i `circle`
(po 142 konstruirana para). Izvorni Datasaurus nacrtao je Alberto Cairo,
a proširenje Datasaurus Dozen objavili su Justin Matejka i George Fitzmaurice
u radu *Same Stats, Different Graphs* (2017), DOI 10.1145/3025453.3025912.
Ovo je ilustracija uz narativ, a ne novi studentski podatkovni paket.
Izvorni retci nisu pohranjeni uz knjigu i nisu potrebni tijekom renderiranja.

Preuzeta je datoteka `inst/extdata/DatasaurusDozen-Long.tsv` iz paketa
datasauRus 0.1.10, commit `269706b98d171fe52258e4a7288e26e1b37512f5`,
27. listopada 2026. Paket i pripadna dokumentacija objavljeni su pod MIT licencom.

- [Prikvačeni izvor](https://raw.githubusercontent.com/jumpingrivers/datasauRus/269706b98d171fe52258e4a7288e26e1b37512f5/inst/extdata/DatasaurusDozen-Long.tsv)
- [Opis paketa](https://github.com/jumpingrivers/datasauRus/blob/269706b98d171fe52258e4a7288e26e1b37512f5/DESCRIPTION)
- [Licenca](https://github.com/jumpingrivers/datasauRus/blob/269706b98d171fe52258e4a7288e26e1b37512f5/LICENSE.md)
- SHA-256 ulaza `c8c4792c3ed15238ba07dad6ab778adc79d72e3e1324ead4d8c1ae52849780f8`

Za ponovnu izradu preuzeti prikvačeni ulaz izvan repozitorija, zatim iz
korijena knjige pokrenuti `python bookwright_plugin/bookwright/scripts/run_rscript.py scripts/build-datasaurus-figure.R <put-do-tsv>`.
Skripta provjerava identitet ulaza, broj točaka i zaokružene sažetke navedene
u prozi. Raspored je autorski, s jednakim osima i bojama iz tokena knjige.
SVG inačice namijenjene su svijetloj i tamnoj temi, PDF tisku.

## MIT License

Copyright (c) 2022 datasauRus authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
