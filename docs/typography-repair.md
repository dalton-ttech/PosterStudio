# Typography Repair

Default first pass includes the full real copy so the image model can design typography and imagery together.

## Repair order

1. If the text is correct, keep it.
2. If only a small amount is wrong, use image edit and change only that text.
3. If exact copy remains unreliable:
   - preserve the generated visual layout,
   - remove/clean the incorrect text region if needed,
   - reproduce the intended text deterministically using a design/compositing tool.

Do not invent pre-generation rules such as:
- light background → dark text
- low contrast → always add a mask
- complex area → always add a panel

Let the image model make the first design decision. Deterministic repair should follow that decision rather than replace it.

For logos, always prefer the supplied original logo file for final output.
