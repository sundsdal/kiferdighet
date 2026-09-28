# Aksel design tokens – hurtigreferanse

Tokens fra `@navikt/ds-tokens` brukes som CSS-variabler. Eksempler:

| Bruk | Token | Feil alternativ |
|---|---|---|
| Standard tekstfarge | `var(--a-text-default)` | `#333333`, `#000` |
| Luft under element | `var(--a-spacing-4)` | `16px` |
| Liten luft | `var(--a-spacing-2)` | `8px` |
| Feilfarge | `var(--a-text-danger)` | `#c30000` |
| Flatefarge | `var(--a-surface-default)` | `#ffffff` |

Regel: finn alltid nærmeste token i Aksel-dokumentasjonen i stedet for å
hardkode verdier. Tokens sikrer at løsningen følger NAVs visuelle profil og
tåler fremtidige designendringer uten kodeendring.
