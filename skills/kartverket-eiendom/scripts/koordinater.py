#!/usr/bin/env python3
"""Koordinathjelper: DMS-konvertering og avstand (haversine).

Eksempler:
  python koordinater.py --dms-til-des 59 54 50 N 10 45 8 E
  python koordinater.py --avstand 59.9139 10.7522 60.3921 5.3221
"""

import argparse
import math

JORDRADIUS_KM = 6371.0


def dms_til_des(grader: float, minutter: float, sekunder: float, retning: str) -> float:
    des = abs(grader) + minutter / 60 + sekunder / 3600
    if retning.upper() in ("S", "W"):
        des = -des
    return round(des, 6)


def haversine_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    b1, b2 = math.radians(lat1), math.radians(lat2)
    db, dl = math.radians(lat2 - lat1), math.radians(lon2 - lon1)
    a = math.sin(db / 2) ** 2 + math.cos(b1) * math.cos(b2) * math.sin(dl / 2) ** 2
    return round(2 * JORDRADIUS_KM * math.asin(math.sqrt(a)), 3)


def main(argv: list | None = None) -> int:
    parser = argparse.ArgumentParser(description="Koordinathjelper")
    parser.add_argument("--dms-til-des", nargs=8, metavar=("G", "M", "S", "R", "G", "M", "S", "R"),
                        help="Bredde- og lengdegrad som DMS, f.eks. 59 54 50 N 10 45 8 E")
    parser.add_argument("--avstand", nargs=4, type=float, metavar=("LAT1", "LON1", "LAT2", "LON2"))
    args = parser.parse_args(argv)

    if args.dms_til_des:
        g1, m1, s1, r1, g2, m2, s2, r2 = args.dms_til_des
        lat = dms_til_des(float(g1), float(m1), float(s1), r1)
        lon = dms_til_des(float(g2), float(m2), float(s2), r2)
        print(f"{lat}, {lon}")
        return 0
    if args.avstand:
        print(f"{haversine_km(*args.avstand)} km")
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
