---
name: lovdata-juridisk-analyse
description: Strukturerer juridiske vurderinger etter norsk rettskildelære og vurderer samsvar mot norsk lovverk, EØS-rett og AI Act. Bruk ved juridiske spørsmål om personvern (GDPR), avtalerett, opphavsrett eller åpenhetskrav for KI-agenter.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# Norsk rettskildeanalyse og samsvarsvurdering

## Formål

Etablere en etterrettelig juridisk resonneringsprosess basert på anerkjent norsk
rettskildelære (se `references/rettskildelaere.md`), samt håndheve gjeldende nasjonale
og europeiske regulatoriske rammer for agentisk programvare (se `references/ai-act.md`).

## Rettskildehierarki

Vurderinger skal ta utgangspunkt i det formelle trinnhøydehierarkiet:

1. Grunnloven
2. Formell lov (vedtatt av Stortinget)
3. Forskrifter (hjemlet i lov)
4. EØS-avtalen og inkorporerte EU-forordninger
5. Rettspraksis fra Norges Høyesterett
6. Lovforarbeider (NOU, proposisjoner til Stortinget)
7. Forvaltningspraksis, juridisk litteratur og sedvane

## Spesifikke vurderinger for KI-agenter og autonomi

### Avtalerett og fullmakt

En KI-agent er ikke et eget rettssubjekt. Disposisjoner utført av agenten tilregnes den
juridiske personen som har satt den i drift, i henhold til avtalelovens alminnelige
regler om fullmakt og ugyldighet (§ 32).

### Åpenhetskrav (AI Act artikkel 50)

- Agenter som kommuniserer direkte med fysiske personer skal deklarere sin syntetiske identitet.
- Det er rettsstridig å utstyre en agent med en konstruert identitet som utgir seg for
  å være et bestemt menneske overfor tredjeparter.

### Personvern og databehandling (GDPR)

Verifiser at agenten ikke mater personidentifiserbare data (herunder fødselsnumre eller
helseopplysninger) inn i globale inferensmodeller uten forankring i behandlingsgrunnlag
(artikkel 6) og databehandleravtale.

## Metodiske feil å unngå

- Unngå henvisninger til opphevet lovgivning; kontroller alltid at lovspeilet refererer
  til gjeldende lov (for eksempel straffeloven av 2005, ikke 1902).
- Flagg rettslig usikkerhet eksplisitt der det foreligger manglende rettspraksis på
  nye agentteknologiske områder.

## Obligatorisk presisering

Analysen skal alltid avsluttes med følgende tekst:

«Dette notatet utgjør en teknisk-juridisk vurdering og erstatter ikke formell
rådgivning fra autorisert advokat.»
