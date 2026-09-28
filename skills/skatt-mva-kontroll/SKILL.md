---
name: skatt-mva-kontroll
description: Beregner norsk merverdiavgift med korrekte satser, kontrollerer bokføringsdata og SAF-T-formatering. Bruk ved spørsmål om MVA-satser, mva-melding, fradrag for inngående avgift eller SAF-T-filer.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# Skatt og MVA-kontroll — Skatteetaten og merverdiavgiftsloven

## Formål

Beregne MVA med riktige satser, kontrollere bokføringsdata før mva-melding og
avdekke formateringsfeil i SAF-T-filer – uten å gjette på satser eller beløpsgrenser.

## Prosedyre

### 1. Fastslå riktig sats

Bruk `references/mva-satser.md`. Norske hovedsatser:

- **25 %** – generell sats (de fleste varer og tjenester)
- **15 %** – næringsmidler
- **12 %** – persontransport, overnatting, kringkasting, kultur og idrett

Ved tvil om hvilken sats som gjelder: si det eksplisitt og vis til skatteetaten.no.
Finn aldri på satser eller unntak.

### 2. Beregn deterministisk

Ikke regn MVA i hodet i fritekst – kjør skriptet:

```bash
python scripts/mva_kalkulator.py --belop <beløp> --sats <25|15|12> [--inkl-mva]
```

Skriptet skriver ut grunnlag, avgiftsbeløp og total, med avrunding til nærmeste øre.

### 3. Kontroller før mva-melding

Gå gjennom sjekklisten punkt for punkt sammen med brukeren:

- Er alle inntekter ført med riktig avgiftskode?
- Er inngående MVA kun fradragsført der fradragsrett foreligger?
- Stemmer summen i regnskapet med det som rapporteres i mva-meldingen?
- Er fristen overholdt (normalt 6 terminer per år – be brukeren bekrefte sin termin)?

### 4. SAF-T-kontroll

Ved SAF-T-filer: verifiser at filen er gyldig XML, at obligatoriske felter
(`Company`, `FiscalYear`, `GeneralLedgerEntries`) finnes, og at saldoer summerer.
Rapporter avvik som nummerert liste med filsti og linjenummer der det er mulig.

## Grenser

- Gi aldri bindende skatteråd – vis alltid til Skatteetaten eller regnskapsfører ved tvil.
- Be aldri om fødselsnummer, passord eller BankID. Nøyer deg med anonymiserte tall.
