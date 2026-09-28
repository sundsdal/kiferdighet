---
name: kartverket-eiendom
description: Slår opp norske eiendommer på gårds- og bruksnummer (gnr/bnr) og avklarer offisielle stedsnavn via Kartverkets tjenester. Bruk ved spørsmål om eiendom, gnr/bnr, matrikkel, grenser eller stedsnavn i Norge.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# Kartverket eiendom — matrikkel og stedsnavn

## Formål

Hjelpe med eiendomsoppslag på gårds- og bruksnummer og avklare offisielle
stedsnavn (SSR), med Kartverkets autoritative tjenester som kilde.

## Prosedyre

### 1. Fastslå hva brukeren har

Spør etter: kommunenummer (4 siffer), gårdsnummer og bruksnummer – eller adresse/stedsnavn
hvis matrikkelnummer mangler. Et fullstendig matrikkelnummer er `Knr-Gnr/Bnr/Fnr/Snr`.

### 2. Oppslag

- **Nettleseroppslag:** bruk Seeiendom (seeiendom.kartverket.no) for visuell kontroll
  av eiendom, grenser og basisinformasjon.
- **Koordinater og avstander:** bruk `scripts/koordinater.py` for deterministiske
  beregninger (desimalgrader ↔ grader/minutter/sekunder, avstand mellom punkter).
- **Stedsnavn:** kontroller skrivemåte mot Sentralt stedsnavnregister (SSR) –
  det er SSR-skrivemåten som er offisiell, ikke den lokale dialektformen.
- **Maskinelle oppslag:** bruk Kartverkets/Geonorges offisielle API-er. Verifiser
  alltid gjeldende endepunkter i `references/matrikkel-felt.md` og Kartverkets
  dokumentasjon før produksjonsbruk – endepunkter endres over tid.

### 3. Tolkning

Se `references/matrikkel-felt.md` for de viktigste matrikkelfeltene
(bruksenhetsnummer, festenummer, seksjonsnummer, skyldmark med mer).

## Grenser

- Matrikkeldata viser registrerte rettigheter og grenser, men erstatter ikke
  tinglyst grunnboksinformasjon ved tvist – vis til grunnboken og eventuelt advokat.
- Del aldri posisjonsdata om andre personer enn brukeren selv.
