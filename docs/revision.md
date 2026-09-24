# Revision Modes

Choose one mode explicitly.

## REGENERATE
Use when the concept or aesthetic result is wrong.

- Start a clean generation context.
- Provide the original reference, brief, exact copy, assets, and latest feedback.
- Do **not** show the failed generation unless a specific property from it must be preserved.

## EDIT
Use when the existing result is broadly correct.

- Use the selected generated image as the edit target.
- Request only the specific change.
- Keep the edit prompt short.
- Prefer one meaningful change at a time when precision matters.

This distinction prevents failed visual decisions from becoming accidental anchors for later generations.
