---
name: met-yr-varsel
description: Henter pålitelige værprognoser og meteorologiske data fra Meteorologisk institutt (MET/Yr) via Locationforecast 2.0. Bruk ved spørsmål om vær, nedbør, vind, temperatur eller historiske værdata for norske koordinater.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# MET Norway / Yr værvarsel — Locationforecast 2.0

## Formål

Hente og tolke værprognoser fra Meteorologisk institutts åpne API under full
etterlevelse av METs tjenestevilkår og identifikasjonsregler
(se `references/brukervilkaar.md`).

## Prosedyre

### 1. Påkrevd klientidentifikasjon

MET Norway krever at alle forespørsler har en unik `User-Agent`-header med kontaktinformasjon.
Forespørsler med standardbiblioteker (som `curl`, `python-requests` eller anonyme klienter)
blokkeres automatisk med HTTP 403.

Format:

```text
User-Agent: MinBedrift-Agent/1.0 kontakt@mittdomene.no
```

### 2. Eksekvering av API-kall

```http
GET https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={breddegrad}&lon={lengdegrad}
```

Bruk `scripts/met_client.py` – den setter korrekt `User-Agent` automatisk:

```bash
python scripts/met_client.py --lat 59.9139 --lon 10.7522 --kontakt kontakt@mittdomene.no
```

Koordinatene må oppgis i WGS84 desimalgrader med maksimalt fire desimalers presisjon.

### 3. Caching og rate limiting

- Les alltid responsheaderen `Expires`.
- Data for samme lokasjon skal aldri etterspørres på nytt før tidspunktet i `Expires`
  er passert. Tjenesten oppdateres normalt hver time.

### 4. Parsing av datastruktur

Naviger til `properties.timeseries[0]` og trekk ut kjernemetrikker:

- Temperatur: `data.instant.details.air_temperature` (°C)
- Vindstyrke: `data.instant.details.wind_speed` (m/s)
- Værsymbol: `data.next_1_hours.summary.symbol_code`
- Nedbør: `data.next_1_hours.details.precipitation_amount` (mm)

## Utdataformat

Presenter svaret oversiktlig med stedsnavn, koordinater, gyldighetsperiode,
temperatur, vindforhold, forventet nedbør og varslet værtype.
