# Generation

## Input contract

Each generation worker should receive only what it needs:
- one primary reference image
- compact poster brief
- exact real copy
- relevant brand asset(s)
- output ratio / size requirement
- one reference mode: `mimic` or `inspired`

Do not automatically include:
- other references
- other workers' generations
- rejected outputs
- the full reference manifest
- Pinterest keyword research
- verbose visual analysis
- unrelated skills/docs

## Isolation

Different reference images must run in separate contexts.

For the same reference, `mimic` and `inspired` comparisons should also run in separate contexts when the goal is a clean A/B comparison.

## First pass

Include all real copy in the first generation. Let the image model make the initial decisions about text placement, contrast, spacing, masks/panels, and integration with imagery.

Do not pre-encode a design rule engine into the prompt.
