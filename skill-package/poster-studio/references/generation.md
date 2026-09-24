# Generation

For each selected reference:
- pass the reference image itself
- pass the concise brief
- pass exact real copy
- pass supplied brand asset(s)
- pass aspect ratio / output requirement

Default mode: `mimic`.
Optional comparison mode: `inspired`.

Do not expand visual analysis into a long prompt.

`mimic`: closely preserve visual language, layout logic, proportions, material feeling, and overall design character while adapting content.

`inspired`: use the reference as the main visual inspiration while allowing a freer new composition.

Run each mode in a separate context when comparing.

Revision:
- REGENERATE = clean context; omit failed output.
- EDIT = use accepted image as edit target and request only the necessary change.
