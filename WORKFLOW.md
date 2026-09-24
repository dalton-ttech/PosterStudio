# PosterStudio Local Workflow

Use this workflow only when the user explicitly starts a poster-design task.

## Core principles

1. **Reference-first.** Do not translate a visual reference into a long image prompt.
2. **Minimal prompting.** Give the image model the task, exact real copy, supplied logo/assets, output ratio, and only essential constraints.
3. **Human-selected references only.** Pinterest discovery is human-curated before anything enters the reference library.
4. **One reference = one isolated generation context.** Workers for different references must not see each other's outputs.
5. **Mimic first, Inspired second.** Default to `mimic`. Run `inspired` in a separate context when comparison is useful.
6. **Image-first typography.** First pass includes the full real copy so the image model designs text and image together.
7. **Repair, don't pre-rule.** Do not preload typography contrast/mask rules. If text is wrong, try image edit; if that fails, repair exact typography afterward while preserving the image model's layout decisions.
8. **Exact logos.** A generated logo is only a layout placeholder. Final brand marks must use the original supplied asset.
9. **No HTML final poster by default.** HTML is allowed for review boards or when the user explicitly asks for HTML editing.
10. **No global agent instructions.** Do not create or depend on a global `AGENTS.md`.

## Phases

### 1. Brief
Create a compact project brief from the user's request. Read `docs/brief.md` only if needed.

### 2. Pinterest research
Generate visual-neighborhood search directions rather than literal intent terms. Read `docs/pinterest-research.md`.

### 3. Human reference selection
Wait for the user to download only the images they like into `private/library/inbox/`.

### 4. Reference import
Run `scripts/import_references.py` to dedupe, rename, and register the selected files. Read `docs/reference-library.md` if classification is needed.

### 5. Generation planning
For each selected reference, create isolated work:
- default: `mimic`
- optional comparison: `inspired`

Use `prompts/mimic.md` or `prompts/inspired.md`. Do not expand them into verbose art-direction prompts.

### 6. First-pass generation
Pass:
- one primary reference image
- relevant brand asset(s)
- full exact copy
- concise brief
- output ratio / size requirement

Do not expose outputs from one reference worker to another.

### 7. Review
Build a contact sheet with `scripts/make_contact_sheet.py`.
Use HTML only if a richer local review board is specifically useful.

### 8. Revision
Choose deliberately:
- `REGENERATE`: new clean context; do not show the failed generation.
- `EDIT`: use the selected generation as the explicit edit target.

Read `docs/revision.md`.

### 9. Typography / logo repair
If image edit cannot reliably fix exact copy, preserve the generated layout and use deterministic repair. Read `docs/typography-repair.md`.

### 10. Export
Use `scripts/export_final.py` for final dimensions and file format.
