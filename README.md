# PosterStudio

Reference-first poster production workflow for Codex.

PosterStudio is designed around a simple principle: **let the reference image carry the visual language; let Codex manage the workflow.** It avoids turning visual references into long, restrictive prompts.

## What it does

- Turns a poster request into Pinterest *visual-neighborhood* search terms.
- Imports only references that a human has already selected.
- Keeps one reference / one generation worker context for clean visual exploration.
- Supports two reference modes:
  - `mimic` — prioritize close visual-language and layout transfer.
  - `inspired` — use the reference as a looser visual starting point.
- Sends the full real copy to the image model in the first pass.
- Uses image editing first for copy corrections; precise typography repair is a fallback.
- Keeps logos, brand source files, reference images, generations, and client assets local by default.
- Provides small local scripts for project setup, reference ingestion, manifests, contact sheets, logo compositing, and 9:16 export.

## Start

1. Clone this repository and open it in Codex Desktop.
2. Read `START_HERE.md`.
3. Put private brand assets under `private/brands/`.
4. Start a poster task by telling Codex:
   `Read WORKFLOW.md and start a new poster project.`

The local workflow does **not** depend on a global AGENTS.md or custom skill.

A lightweight shareable skill package is included under `skill-package/poster-studio/` for later packaging.

## Privacy

This repository is intentionally safe to publish. Private/local assets are excluded by `.gitignore`, including:

- brand logos and VI source files
- Pinterest/reference images
- generated poster images
- client assets
- project outputs

See `docs/privacy-and-assets.md`.
