---
name: sync-viewer-publish
description: Use when work in `cli/src/prototype/viewer` needs to be synchronized into the root `viewer-publish/` app, especially after UI/style changes, shared component updates, static asset updates, or when someone asks to "sync viewer to publish-viewer", "同步 viewer 到 viewer-publish", or refresh the publish viewer and validate the build without overwriting publish-only logic.
---

# Sync Viewer Publish

## Overview

This skill keeps the shared parts of `cli/src/prototype/viewer/` and `viewer-publish/` aligned while protecting publish-only files such as Docker config, artifact serving logic, and read-only app behavior.

Use it when:

- shared styles or assets changed in `viewer`
- common components need to be copied into `viewer-publish`
- someone asks to sync `viewer` into `viewer-publish`
- you need a safe sync plus a build check for `viewer-publish`

## Workflow

1. Start at the repo root.
2. Run the sync script in dry-run mode first.
3. Review the manual-merge list from [references/scope.md](references/scope.md).
4. Apply the sync.
5. If the task asks to verify, run `pnpm install` and `pnpm build` inside `viewer-publish/`.
6. Report which files were copied automatically and which publish-only files still need manual review.

## Commands

Dry run:

```bash
python3 skills/sync-viewer-publish/scripts/sync_viewer_publish.py
```

Apply sync:

```bash
python3 skills/sync-viewer-publish/scripts/sync_viewer_publish.py --apply
```

Apply and verify build:

```bash
python3 skills/sync-viewer-publish/scripts/sync_viewer_publish.py --apply --install --build
```

## Guardrails

- Do not replace `viewer-publish/scripts/serve.mjs`, `Dockerfile`, `docker-compose.yml`, `weblist/`, or other publish-only files.
- Do not blindly overwrite files listed as manual merge targets in [references/scope.md](references/scope.md).
- If `viewer` changed `App.tsx`, `Preview.tsx`, `FileTree.tsx`, `Header.tsx`, `MarkPanel.tsx`, `types.ts`, `package.json`, `vite.config.ts`, or `tsconfig.json`, inspect and merge intentionally.
- Prefer the script for deterministic copying instead of ad hoc shell commands.

## Resources

### scripts/

- `sync_viewer_publish.py`: dry-run/apply sync script, optional install/build verification

### references/

- `scope.md`: documents which files are auto-mirrored and which require manual merge
