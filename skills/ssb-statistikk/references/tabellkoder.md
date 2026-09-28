# SSB-tabellkoder

Mest brukte tabeller for denne ferdigheten. Verifiser alltid at tabell-ID-en
fortsatt er gyldig på ssb.no før større analyser – SSB flytter av og til tabeller.

| Tabell | Innhold |
|---|---|
| 03013 | Konsumprisindeksen (KPI), totalindeks og delindekser |
| 07459 | Befolkning på kommunenivå |
| 11418 | Gjennomsnittlig månedslønn etter næring |

Spørringer sendes som HTTP POST med `Content-Type: application/json` til
`https://data.ssb.no/api/v0/no/table/{tabell_id}`. Maks 800 000 celler per spørring –
begrens `Tid`-utvalget til relevante årsmåneder.
