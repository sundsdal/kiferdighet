#!/usr/bin/env python3
"""Deterministisk MVA-kalkulator for norske satser.

Eksempler:
  python mva_kalkulator.py --belop 1000 --sats 25
  python mva_kalkulator.py --belop 1250 --sats 25 --inkl-mva
"""

import argparse
from decimal import Decimal, ROUND_HALF_UP

GYLDIGE_SATSER = (Decimal("25"), Decimal("15"), Decimal("12"))


def beregn(belop: Decimal, sats: Decimal, inkl_mva: bool) -> dict:
    ore = Decimal("0.01")
    if inkl_mva:
        total = belop.quantize(ore, rounding=ROUND_HALF_UP)
        grunnlag = (belop / (1 + sats / 100)).quantize(ore, rounding=ROUND_HALF_UP)
        avgift = total - grunnlag
    else:
        grunnlag = belop.quantize(ore, rounding=ROUND_HALF_UP)
        avgift = (belop * sats / 100).quantize(ore, rounding=ROUND_HALF_UP)
        total = grunnlag + avgift
    return {"grunnlag": grunnlag, "avgift": avgift, "total": total}


def main(argv: list | None = None) -> int:
    parser = argparse.ArgumentParser(description="Norsk MVA-kalkulator")
    parser.add_argument("--belop", type=Decimal, required=True)
    parser.add_argument("--sats", type=Decimal, required=True, help="25, 15 eller 12")
    parser.add_argument("--inkl-mva", action="store_true", help="Beløpet er inkl. MVA")
    args = parser.parse_args(argv)

    if args.sats not in GYLDIGE_SATSER:
        parser.error(f"Ugyldig sats {args.sats} – gyldige satser: 25, 15, 12")
    resultat = beregn(args.belop, args.sats, args.inkl_mva)
    print(f"Sats: {args.sats} % ({'inkl.' if args.inkl_mva else 'ekskl.'} MVA)")
    print(f"Grunnlag: {resultat['grunnlag']} kr")
    print(f"MVA: {resultat['avgift']} kr")
    print(f"Totalt: {resultat['total']} kr")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
