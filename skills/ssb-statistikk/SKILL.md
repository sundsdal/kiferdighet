---
name: ssb-statistikk
description: Henter, transformerer og analyserer offisiell norsk statistikk fra Statistisk sentralbyrå (SSB) via PxWebApi. Bruk ved spørsmål om konsumprisindeksen (KPI), prisjustering, lønnsstatistikk eller befolkningsdata i Norge.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# SSB Statistikk — PxWebApi, konsumprisindeks og analyse

## Formål

Trekke ut autoritative tabellserier fra SSB for å utføre inflasjonsjusteringer,
lønnsanalyser og demografiske beregninger – uten å generere hallusinerte statistikkdata.

## Prosedyre

### 1. Tabellutvelgelse

- Konsumprisindeksen (totalindeks og delindekser): Tabell **03013**
- Befolkning på kommunenivå: Tabell **07459**
- Gjennomsnittlig månedslønn etter næring: Tabell **11418**
- Se `references/tabellkoder.md` dersom andre spesialiserte serier etterspørres.

### 2. Spørring mot PxWebApi

Send HTTP POST-forespørsel:

```http
POST https://data.ssb.no/api/v0/no/table/{tabell_id}
Content-Type: application/json
```

Spørrekroppen må spesifisere variablene for `Tid`, `ContentsCode` og filter.
Begrens forespørselen til relevante årsmåneder for å unngå overskridelse av
cellerestriksjonene (maksimum 800 000 celler per spørring).

### 3. Beregning av KPI-justerte beløp

For justering av pengebeløp fra basisperiode til målperiode benyttes formelen:

```text
Justert verdi = Opprinnelig beløp × (KPI_slutt / KPI_start)
```

Ikke overlat flyttallsaritmetikk til språkmodellens egen tekstgenerering – kjør skriptet:

```bash
python scripts/pxweb_client.py --calc-kpi --amount <beløp> --from <år-mnd> --to <år-mnd>
```

## Begrensninger og tolkning

- Konsumprisindeksen publiseres normalt den 10. i hver måned.
- Det er aldri tillatt å ekstrapolere eller estimere indekser for fremtidige måneder
  uten å opplyse om at det utgjør en usikker prognose.

## Utdataformat

Svaret skal presentere tabellnummer, datapunkt for opprinnelig tidspunkt, datapunkt for
sluttidspunkt, beregnet inflasjonssats i prosent samt det endelig inflasjonsjusterte kronebeløpet.
