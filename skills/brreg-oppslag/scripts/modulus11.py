#!/usr/bin/env python3
"""Validerer norsk organisasjonsnummer med Modulus 11.

Bruk: python modulus11.py <organisasjonsnummer>
Returnerer 0 (gyldig) eller 1 (ugyldig) og skriver resultatet til stdout.
"""

import sys

VEKTER = (3, 2, 7, 6, 5, 4, 3, 2)


def valider(orgnr: str) -> bool:
    """Returnerer True dersom orgnr er 9 siffer med gyldig kontrollsiffer."""
    if len(orgnr) != 9 or not orgnr.isdigit():
        return False
    siffer = [int(c) for c in orgnr]
    total = sum(s * v for s, v in zip(siffer[:8], VEKTER))
    rest = total % 11
    if rest == 0:
        kontroll = 0
    elif rest == 1:
        return False  # Kontrollsiffer ville blitt 10 – ugyldig nummer
    else:
        kontroll = 11 - rest
    return kontroll == siffer[8]


def main(argv: list) -> int:
    if len(argv) != 2:
        print("Bruk: python modulus11.py <organisasjonsnummer>", file=sys.stderr)
        return 2
    orgnr = argv[1].strip().replace(" ", "")
    if valider(orgnr):
        print(f"{orgnr}: gyldig organisasjonsnummer")
        return 0
    print(f"{orgnr}: UGYLDIG kontrollsiffer", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
