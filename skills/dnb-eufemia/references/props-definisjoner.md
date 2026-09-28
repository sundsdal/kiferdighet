# Eufemia props og validering – hurtigreferanse

Generelle regler for prop-validering mot `@dnb/eufemia`:

1. **Labels er påkrevde.** Alle skjemakomponenter skal ha `label`. Placeholder
   er ikke en erstatning for label.
2. **Feiltilstand via status.** Bruk `status` + `status_state="error"` sammen med
   `FormStatus` for feilmeldinger – ikke egne fargekoder.
3. **Kontrollerte verdier.** Bruk `value` + `on_change` (kontrollerte komponenter)
   i skjemaer som skal valideres eller sendes inn.
4. **Dato og tall.** `DatePicker` forventer ISO-dato; tallfelt valideres som tall,
   ikke som tekst – konverter før innsending.
5. **Opplasting.** `Upload` krever aksepterte filtyper og maksstørrelse eksplisitt satt.
6. **Tilgjengelighet.** Behold standard tastaturstøtte og fokusrekkefølge –
   `tabindex`-triksing er forbudt uten dokumentert behov.

Ved uenighet mellom denne filen og eufemia.dnb.no gjelder alltid den offisielle
dokumentasjonen.
