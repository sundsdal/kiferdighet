#!/usr/bin/env bash
# Deploi deploy-mal – TILPASS til din app og verifiser mot deploi.no før bruk.
# Krever: DEPLOI_TOKEN i miljøet. Kjør aldri med -y/flagg som hopper over bekreftelser.
set -euo pipefail

: "${DEPLOI_TOKEN:?Sett DEPLOI_TOKEN i miljøet først}"
MILJO="${1:-test}"

echo "== Bygg =="
# Eksempel – bytt ut med appens faktiske byggesteg:
# bun run build

echo "== Deploy til miljø: $MILJO =="
# Eksempel – bytt ut med Deplois gjeldende CLI/API-kall:
# deploi deploy --env "$MILJO"

echo "== Verifiser helsesjekk =="
# Eksempel:
# curl -fsS "https://$MILJO.minapp.no/internal/isready"

echo "Deploy fullført. Husk å notere server, tidspunkt og kommandoer i svaret."
