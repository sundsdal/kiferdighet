---
name: dnb-eufemia
description: Veileder komponentvalg og prop-validering mot DNBs designsystem Eufemia. Bruk ved frontend-oppgaver som bruker @dnb/eufemia – skjemakomponenter, validering, tilgjengelighet eller sammensetting av applikasjonsmoduler.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# DNB Eufemia — komponentvalg og prop-validering

## Formål

Sikre at React-kode som bruker DNBs designsystem Eufemia følger bankens
retningslinjer for komponentbruk, skjemaer og tilgjengelighet.

## Prosedyre

### 1. Velg riktig komponent

Bruk Eufemias egne komponenter fremfor generiske HTML-elementer eller andre biblioteker:

- Skjema: `Input`, `Dropdown`, `Radio`, `Checkbox`, `DatePicker`, `Upload`
- Tilbakemelding: `FormStatus`, `Modal`, `Drawer`, `Tooltip`
- Layout og typografi: `Section`, `Heading`, `P`, `Space`
- Se `references/props-definisjoner.md` for valideringsregler per komponenttype.

### 2. Valider props

- Sjekk at påkrevde props er satt og at verdityper stemmer før koden anses som ferdig.
- Bruk `FormStatus`/`FormRow` for feilmeldinger – aldri egne fargede tekstdiver.
- Ikke overstyr innebygde ARIA-attributter med egne løsninger.

### 3. Skjemaflyt og tilgjengelighet

- Alle felter skal ha synlig `label` koblet til input.
- Validering skal skje både ved utfylling og ved innsending, med feilmeldinger
  som peker konkret på feltet og hvordan feilen rettes.
- Følg Eufemias retningslinjer for universell utforming – se offisiell
  dokumentasjon på eufemia.dnb.no ved tvil. Dokumentasjonen er fasit hvis denne
  ferdigheten og docs er uenige.

## Grenser

Denne ferdigheten dekker designsystem-bruk, ikke bankfaglige vurderinger
(renter, produkter, rådgivning). Henvis alltid til DNBs offisielle kanaler for det.
