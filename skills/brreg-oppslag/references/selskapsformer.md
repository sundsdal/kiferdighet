# Selskapsformer i Enhetsregisteret

Utdrag av de vanligste `organisasjonsform.kode`-verdiene fra Brønnøysundregistrene.
Full liste finnes i Enhetsregisterets API-dokumentasjon.

| Kode | Betegnelse | Kort forklaring |
|---|---|---|
| AS | Aksjeselskap | Begrenset personlig ansvar, krav til aksjekapital |
| ENK | Enkeltpersonforetak | Personlig ansvar, én eier |
| NUF | Norskregistrert utenlandsk foretak | Utenlandsk selskap registrert i Norge |
| DA | Ansvarlig selskap med delt ansvar | Deltakerne hefter for sin andel |
| ANS | Ansvarlig selskap med solidaransvar | Deltakerne hefter solidarisk |
| ASA | Allmennaksjeselskap | Børsnoterte/større aksjeselskap |
| SA | Samvirkeforetak | Eid og styrt av medlemmene/brukerne |
| STI | Stiftelse | Selveiende formuesmasse med et formål |
| KF | Kommunalt foretak | Eid av kommune |
| FKF | Fylkeskommunalt foretak | Eid av fylkeskommune |
| ORG | Forening/lag/innretning | Frivillige organisasjoner |
| BBL | Boligbyggelag | Forvaltning av boliger |
| BRL | Borettslag | Beboere eier andeler |

Merk: Koden alene sier ikke om foretaket er aktivt – sjekk alltid
`slettedato`, `konkurs` og `underAvvikling` i API-responsen.
