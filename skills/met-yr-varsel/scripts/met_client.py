#!/usr/bin/env python3
"""Klient for MET Locationforecast 2.0 med påkrevd identifikasjon og caching-merknad.

Eksempel:
  python met_client.py --lat 59.9139 --lon 10.7522 --kontakt kontakt@mittdomene.no
"""

import argparse
import json
import sys
import urllib.request

ENDEPUNKT = "https://api.met.no/weatherapi/locationforecast/2.0/compact"


def hent(lat: float, lon: float, kontakt: str) -> tuple:
    url = f"{ENDEPUNKT}?lat={lat:.4f}&lon={lon:.4f}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": f"kiferdigheter-met-client/1.0 {kontakt}"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        expires = resp.headers.get("Expires", "ukjent")
        data = json.loads(resp.read().decode("utf-8"))
        return data, expires


def sammendrag(data: dict) -> dict:
    serie = data["properties"]["timeseries"][0]
    instant = serie["data"]["instant"]["details"]
    neste = serie["data"].get("next_1_hours", {})
    return {
        "tidspunkt": serie["time"],
        "temperatur_c": instant.get("air_temperature"),
        "vind_mps": instant.get("wind_speed"),
        "symbol": (neste.get("summary") or {}).get("symbol_code"),
        "nedbor_mm": (neste.get("details") or {}).get("precipitation_amount"),
    }


def main(argv: list | None = None) -> int:
    parser = argparse.ArgumentParser(description="MET Locationforecast-klient")
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--kontakt", required=True, help="E-post i User-Agent (påkrevd av MET)")
    args = parser.parse_args(argv)

    try:
        data, expires = hent(args.lat, args.lon, args.kontakt)
    except Exception as exc:  # HTTP 403 = mangelfull identifikasjon
        print(f"Feil ved oppslag: {exc}", file=sys.stderr)
        return 1
    resultat = sammendrag(data)
    resultat["expires"] = expires
    resultat["cache_merknad"] = "Ikke spør om samme lokasjon på nytt før Expires."
    print(json.dumps(resultat, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
