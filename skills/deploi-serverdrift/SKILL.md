---
name: deploi-serverdrift
description: Provisjonerer og administrerer norske virtuelle servere hos Deploi via terminalen. Bruk ved spørsmål om Deploi-servere, deploy av apper, serverstatus eller DNS/oppsett hos Deploi.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# Deploi serverdrift — provisjonering og administrasjon

## Formål

Sette kodingsagenter i stand til å provisjonere og drifte virtuelle servere hos
norske Deploi direkte fra terminalen, etter leverandørens dokumentasjon.

## Prosedyre

### 1. Verifiser forutsetninger

- Sjekk at brukeren har en Deploi-konto og tilgangsnøkkel/API-token på plass.
- Les `references/api-referanse.md` og – ved uenighet – Deplois offisielle
  dokumentasjon på deploi.no. Dokumentasjonen er alltid fasit.
- Be aldri om å få tilsendt passord eller tokens i klartekst i chatten;
  brukeren legger dem i miljøvariabler.

### 2. Standard deploy-flyt

Ta utgangspunkt i `scripts/deploy.sh` (mal – tilpass til appen):

1. Bygg applikasjonen lokalt og verifiser at bygget lykkes.
2. Opprett/velg server og miljø etter behov (prod/test).
3. Last opp og start appen; verifiser helsesjekk før trafikk rutes.
4. Rull tilbake ved feil – aldri la et feilet deploy stå som «nesten ferdig».

### 3. Drift og feilsøking

- Sjekk serverstatus og logger før du endrer konfigurasjon.
- Endre én ting av gangen og verifiser mellom hvert steg.
- Dokumenter hva som ble endret (server, tidspunkt, kommando) i svaret til brukeren.

## Grenser

- Kjør aldri destruktive kommandoer (sletting av servere, disker eller DNS-soner)
  uten eksplisitt bekreftelse fra brukeren i samme sesjon.
- Gjett aldri på priser eller kapasitetsgrenser – vis til deploi.no.
