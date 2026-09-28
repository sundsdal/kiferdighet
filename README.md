# KI-ferdigheter.no 🇳🇴

Norsk katalog over **AI-ferdigheter** (*skills*) – gjenbrukbare instruksjoner som gjør KI-assistenter
gode på norske oppgaver: NAV-brev, skattemelding, nynorsk, møtereferat og mer.

Alle ferdigheter er på **norsk** og følger den åpne
[Agent Skills-spesifikasjonen](https://agentskills.io/specification) (`SKILL.md`),
så samme ferdighet virker i **Claude**, **ChatGPT** og **Gemini**.

Nettside: **kiferdigheter.no** (denne repoen bygger både nettsiden og selve ferdighetskilden).

## Hva er en ferdighet?

En **ferdighet** er en mappe med en `SKILL.md`-fil: YAML-frontmatter (`name`, `description`)
pluss Markdown-instruksjoner som assistenten følger når oppgaven dukker opp.

- I **Claude** heter det **skill** (og *plugin marketplace* for distribusjon).
- I **ChatGPT** heter det også **skills** (samme `SKILL.md`-format).
- I **Gemini** heter det **skills** (samme `SKILL.md`-format).

Les mer på nettsiden: [Hva er en ferdighet?](index.html#hva-er-ferdighet).

## Bruk ferdighetene

### Claude Code (anbefalt kilde)

Legg til dette repoet som kilde én gang:

```bash
/plugin marketplace add sundsdal/kiferdighet
/plugin install kiferdigheter
```

Deretter aktiveres ferdighetene automatisk ut fra beskrivelsen, eller eksplisitt med `/<ferdighet-navn>`.

### Claude (app/nett)

Kopier innholdet i ønsket `skills/<navn>/SKILL.md` inn i en egen *skill*,
eller last ned mappen og legg den under `~/.claude/skills/<navn>/`.

### ChatGPT

Legg `SKILL.md`-innholdet som instruksjon i en egen GPT,
eller legg mappen under `~/.agents/skills/<navn>/` for Codex/CLI-bruk.

### Gemini

Kopier mappen til `~/.gemini/skills/<navn>/` (eller `.agents/skills/<navn>/`):

```bash
cp -R skills/nynorsk-korrektur ~/.gemini/skills/nynorsk-korrektur
```

Full guide: [Slik installerer du](index.html#installer).

## Ferdigheter i katalogen

| Ferdighet | Hva den gjør | Tagger |
|---|---|---|
| [nynorsk-korrektur](skills/nynorsk-korrektur/SKILL.md) | Retter bokmål/talemål til korrekt nynorsk | språk, korrektur, nynorsk |
| [skattemelding-hjelp](skills/skattemelding-hjelp/SKILL.md) | Hjelper med norsk skattemelding og fradrag | skatt, økonomi, offentlig |
| [nav-brevhjelp](skills/nav-brevhjelp/SKILL.md) | Skriver og forklarer NAV-brev i klar norsk | nav, offentlig, brev |
| [mote-referat](skills/mote-referat/SKILL.md) | Skriver strukturerte møtereferater på norsk | jobb, produktivitet, møte |

Maskinlesbar katalog: [skills.json](skills.json) (brukes av nettsiden).

## Legg til en ferdighet

1. Lag `skills/<navn>/SKILL.md` etter [Agent Skills-spec](https://agentskills.io/specification):
   - `name` = mappenavnet (små bokstaver, tall, bindestrek, maks 64 tegn).
   - `description` = hva den gjør + når den skal brukes (maks 1024 tegn).
   - Brødtekst på **norsk** med konkrete instruksjoner.
2. Legg til innslag i [skills.json](skills.json) (navn, beskrivelse, tagger, versjon, sti).
3. Kjør validering: `bun run valider`.
4. Send pull request. Tilbakemeldinger håndteres via GitHub Issues (vurderinger/stjerner er droppet for nå).

## Utvikling

Krav: [Bun](https://bun.sh) 1.2+.

```bash
bun install
bun run valider      # validerer alle SKILL.md + skills.json
bun run sjekk        # biome + tsgo
bunx biome check .   # lint/format
bunx tsgo --noEmit   # typesjekk
```

Nettsiden er statisk (`index.html`, `styles.css`, `app.js`) – åpne `index.html` eller tjen med `bunx serve .`.
