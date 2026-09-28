---
name: nav-aksel-utvikling
description: Veileder utvikling av frontend-grensesnitt med NAVs Aksel Designsystem og NAIS-applikasjonskonfigurasjoner. Bruk ved kodeoppgaver med React-komponenter for NAV, universell utforming (WCAG), Aksel design tokens eller NAIS manifest-filer.
license: MIT
metadata:
  author: KI-ferdigheter.no
  version: "1.0"
---

# NAV Aksel og NAIS utviklingsstandard

## Formål

Veilede agenten i korrekt implementasjon av React-grensesnitt med NAVs designsystem
(Aksel), samt generering av kompatible NAIS Kubernetes-spesifikasjoner.

## Retningslinjer for grensesnittutvikling

### Bruk av design tokens

Bruk aldri hardkodede pikselverdier eller tilfeldige hex-koder for farger, luft eller
typografi. Benytt utelukkende tokens fra `@navikt/ds-tokens` via CSS-variabler
(se `references/tokens.md`):

```css
/* Riktig */
margin-bottom: var(--a-spacing-4); color: var(--a-text-default);

/* Feil */
margin-bottom: 16px; color: #333333;
```

### Komponentbruk og universell utforming (WCAG)

Bygg skjemaer og brukergrensesnitt med primitive komponenter fra `@navikt/ds-react`:

- Skjemaelementer: `TextField`, `Select`, `RadioGroup`, `CheckboxGroup`
- Tilbakemeldinger: `Alert`, `GuidePanel`, `Modal`
- Typografi: `Heading`, `BodyLong`, `BodyShort`

Ikke overstyr innebygde ARIA-attributter i Aksel-komponentene med egne løsninger.

### NAIS deploy-konfigurasjon (nais.yaml)

Ta utgangspunkt i `assets/nais-mal.yaml`. Manifestet må validere mot NAIS JSON-skjemaet.

- Sørg for at helsesjekk-probes er definert (`liveness.path`, `readiness.path`).
- Sett ressursforespørsler og begrensninger (`resources.limits` og `resources.requests`)
  eksplisitt for minne og CPU.

## Vanlige fallgruver

- Ikke bland Tailwind CSS-klasser inn i Aksel-komponenter der Aksels spacing-tokens er påkrevd.
- Ikke sett `autoComplete="off"` på fødselsnummer- eller adressefelter uten særskilt
  begrunnelse, da dette bryter WCAG 2.1-kravene.
