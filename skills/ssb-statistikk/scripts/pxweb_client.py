#!/usr/bin/env python3
"""Hjelper for SSB PxWebApi: KPI-justering og enkle tabellspørringer.

Eksempler:
  python pxweb_client.py --calc-kpi --amount 100000 --from 2020-01 --to 2024-01
  python pxweb_client.py --query 03013 --tid 2024-01 --tid 2024-02
"""

import argparse
import json
import sys
import urllib.request

BASE = "https://data.ssb.no/api/v0/no/table"


def post_json(url: str, payload: dict) -> dict:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def normaliser_tid(tid: str) -> str:
    """Godtar '2020-01' eller '2020M01', returnerer SSBs 'YYYYMmm'-format."""
    tid = tid.strip()
    if len(tid) == 7 and tid[4] == "-":
        return tid[:4] + "M" + tid[5:]
    return tid


def hent_kpi(tabell: str, tidspunkt: list) -> dict:
    """Henter totalindeksen (Konsumgrp TOTAL, KpiIndMnd) for gitte tidspunkter."""
    payload = {
        "query": [
            {"code": "Konsumgrp", "selection": {"filter": "item", "values": ["TOTAL"]}},
            {"code": "ContentsCode", "selection": {"filter": "item", "values": ["KpiIndMnd"]}},
            {"code": "Tid", "selection": {"filter": "item", "values": tidspunkt}},
        ],
        "response": {"format": "json"},
    }
    return post_json(f"{BASE}/{tabell}", payload)


def calc_kpi(amount: float, fra: str, til: str, tabell: str = "03013") -> None:
    fra, til = normaliser_tid(fra), normaliser_tid(til)
    data = hent_kpi(tabell, [fra, til])
    verdier = {}
    for rad in data.get("data", []):
        for nokkel in rad.get("key", []):
            if nokkel in (fra, til):
                verdier[nokkel] = float(rad["values"][0])
    if fra not in verdier or til not in verdier:
        print(f"Fant ikke KPI-verdier for {fra} og {til}.", file=sys.stderr)
        raise SystemExit(1)
    kpi_start = verdier[fra]
    kpi_slutt = verdier[til]
    justert = amount * (kpi_slutt / kpi_start)
    inflasjon = (kpi_slutt / kpi_start - 1) * 100
    print(f"Tabell: {tabell}")
    print(f"KPI {fra}: {kpi_start}")
    print(f"KPI {til}: {kpi_slutt}")
    print(f"Inflasjon: {inflasjon:.2f} %")
    print(f"Justert beløp: {justert:,.2f} kr".replace(",", " "))


def main(argv: list | None = None) -> int:
    parser = argparse.ArgumentParser(description="SSB PxWebApi-hjelper")
    parser.add_argument("--calc-kpi", action="store_true", help="KPI-juster et beløp")
    parser.add_argument("--amount", type=float, default=0.0)
    parser.add_argument("--from", dest="fra", default="")
    parser.add_argument("--to", dest="til", default="")
    parser.add_argument("--query", default="", help="Tabell-ID for rå spørring")
    parser.add_argument("--tid", action="append", default=[], help="Tidspunkt, kan gjentas")
    args = parser.parse_args(argv)

    if args.calc_kpi:
        if not (args.amount and args.fra and args.til):
            parser.error("--calc-kpi krever --amount, --from og --to")
        calc_kpi(args.amount, args.fra, args.til)
        return 0
    if args.query:
        print(json.dumps(hent_kpi(args.query, args.tid or []), indent=2, ensure_ascii=False))
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
