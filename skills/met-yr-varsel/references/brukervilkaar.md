# METs brukervilkår – kortversjon

- Alle kall mot `api.met.no` krever unik `User-Agent` med applikasjonsnavn,
  versjon og kontakt-e-post. Anonyme klienter blokkeres med HTTP 403.
- Respekter `Expires`-headeren: cache responsen og spør ikke på nytt for samme
  lokasjon før utløpstidspunktet. Oppdateringer skjer normalt hver time.
- Oppgi koordinater med maks fire desimaler – høyere presisjon gir ikke bedre data.
- Ved høy trafikk: implementer eksponentiell backoff og vurder å cache på tvers
  av brukere for populære lokasjoner.
- Les alltid gjeldende vilkår på api.met.no før produksjonsbruk – vilkårene kan endres.
