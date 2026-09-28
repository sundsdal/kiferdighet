/**
 * Validerer alle skills mot Agent Skills-spec + skills.json-katalogen.
 * Kjør med: bun run valider
 */
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const ROT = new URL("..", import.meta.url).pathname;
const SKILLS_DIR = join(ROT, "skills");

const NAVN_REGEX = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

type Feil = string;
const feil: Feil[] = [];

function parseFrontmatter(innhold: string): Record<string, string> | null {
  const match = innhold.match(/^---\n([\s\S]*?)\n---\n/);
  if (!match) return null;
  const data: Record<string, string> = {};
  for (const linje of match[1].split("\n")) {
    const m = linje.match(/^([a-z-]+):\s*(.+)$/);
    if (m) data[m[1]] = m[2].trim().replace(/^"|"$/g, "");
  }
  return data;
}

const mapper = readdirSync(SKILLS_DIR, { withFileTypes: true })
  .filter((d) => d.isDirectory())
  .map((d) => d.name)
  .sort();

if (mapper.length === 0) feil.push("skills/: ingen ferdigheter funnet");

for (const navn of mapper) {
  const fil = join(SKILLS_DIR, navn, "SKILL.md");
  if (!existsSync(fil)) {
    feil.push(`${navn}: mangler SKILL.md`);
    continue;
  }
  const innhold = readFileSync(fil, "utf8");
  const fm = parseFrontmatter(innhold);
  if (!fm) {
    feil.push(`${navn}: mangler YAML-frontmatter (--- ... ---)`);
    continue;
  }
  if (fm.name !== navn)
    feil.push(`${navn}: name '${fm.name}' må være lik mappenavnet`);
  if (fm.name && (!NAVN_REGEX.test(fm.name) || fm.name.length > 64)) {
    feil.push(
      `${navn}: name bryter spec (små bokstaver/tall/bindestreker, maks 64 tegn)`,
    );
  }
  if (!fm.description) {
    feil.push(`${navn}: description mangler (påkrevd)`);
  } else if (fm.description.length > 1024) {
    feil.push(`${navn}: description er over 1024 tegn`);
  }
  const body = innhold.replace(/^---\n[\s\S]*?\n---\n/, "").trim();
  if (body.length < 100)
    feil.push(`${navn}: brødteksten er mistenkelig kort (< 100 tegn)`);
}

// Sjekk katalogen
const katalogFil = join(ROT, "skills.json");
if (!existsSync(katalogFil)) {
  feil.push("skills.json mangler");
} else {
  const katalog = JSON.parse(readFileSync(katalogFil, "utf8")) as {
    ferdigheter: { navn: string; sti: string; tagger: string[] }[];
  };
  const katalogNavn = new Set(katalog.ferdigheter.map((f) => f.navn));
  for (const navn of mapper) {
    if (!katalogNavn.has(navn))
      feil.push(`skills.json mangler innslag for '${navn}'`);
  }
  for (const f of katalog.ferdigheter) {
    if (!mapper.includes(f.navn))
      feil.push(`skills.json peker på ukjent mappe '${f.navn}'`);
    if (!existsSync(join(ROT, f.sti)))
      feil.push(`skills.json: sti finnes ikke: ${f.sti}`);
    if (!f.tagger || f.tagger.length === 0)
      feil.push(`${f.navn}: mangler tagger i katalogen`);
  }
}

// Sjekk marketplace-manifest
for (const fil of [
  ".claude-plugin/marketplace.json",
  ".claude-plugin/plugin.json",
]) {
  if (!existsSync(join(ROT, fil))) feil.push(`${fil} mangler`);
}

if (feil.length > 0) {
  console.error(
    `Validering feilet (${feil.length} feil):\n- ${feil.join("\n- ")}`,
  );
  process.exit(1);
}

console.log(`OK: ${mapper.length} ferdigheter validert (${mapper.join(", ")})`);
