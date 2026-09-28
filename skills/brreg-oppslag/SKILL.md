---
name: brreg-oppslag
description: Slår opp norske virksomheter, organisasjonsnumre, selskapsformer og regnskapsstatus i Brønnøysundregistrenes åpne data-API-er. Bruk ved spørsmål om norske selskaper, organisasjonsnummer, styre og roller eller selskapsadresser.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# Brreg-oppslag — Enhetsregisteret og Foretaksregisteret

## Formål

Hente autoritative virksomhetsdata fra Brønnøysundregistrenes åpne REST-endepunkter,
og sikre at organisasjonsnumre valideres matematisk før spørring.

## Prosedyre

### 1. Validering av identifikator

Undersøk om brukeren oppgir et organisasjonsnummer (9 siffer) eller et foretaksnavn.

Dersom et 9-sifret nummer er oppgitt, valider kontrollsifferet deterministisk først:

```bash
python scripts/modulus11.py <organisasjonsnummer>
```

Dersom skriptet returnerer ugyldig kontrollsiffer, avbryt forespørselen umiddelbart
og informer brukeren – ikke send nettverkskall med et nummer som er matematisk ugyldig.

### 2. Eksekvering av API-spørring

Direkteoppslag på organisasjonsnummer mot Enhetsregisteret:

```http
GET https://data.brreg.no/enhetsregisteret/api/enheter/{organisasjonsnummer}
```

Dersom oppslaget returnerer HTTP 404, søk i Underenheter:

```http
GET https://data.brreg.no/enhetsregisteret/api/underenheter/{organisasjonsnummer}
```

Ved søk etter firmanavn benyttes søkeendepunktet med paginering:

```http
GET https://data.brreg.no/enhetsregisteret/api/enheter?navn={sokestreng}&size=5
```

### 3. Datauttrekk og analyse

Ekstraher følgende obligatoriske felter:

- `navn` (fullt foretaksnavn)
- `organisasjonsnummer`
- `organisasjonsform.kode` (f.eks. AS, ENK, NUF, DA, ANS – se `references/selskapsformer.md`)
- `forretningsadresse` (gateadresse, postnummer og poststed)
- `registrertIMvaregisteret` (sjekk om enheten har MVA-plikt)
- `konkurs` og `underAvvikling` (status for insolvens eller opphør)

## Kritiske feilkilder

- Foretak med feltet `slettedato` er avviklet og kan ikke inngå i nye avtaler eller faktureres.
- Underenheter (virksomheter) har egne organisasjonsnumre, men kan ikke være juridisk
  part i rettssaker eller kontrakter uten at overordnet enhet involveres.

## Utdataformat

Strukturer svaret slik:

```text
Virksomhet: [Juridisk navn]
Organisasjonsnummer: [9 siffer]
Selskapsform: [Kode og beskrivelse]
Status: [Aktiv / Konkurs / Under avvikling / Slettet]
MVA-registrering: [Registrert / Ikke registrert]
Forretningsadresse: [Adresse, Postnr Poststed]
```
