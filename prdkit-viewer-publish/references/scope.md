# Sync Scope

## Auto-mirrored files

These paths are safe to copy directly from `cli/src/prototype/viewer/` to `viewer-publish/`:

- `public/favicon.svg`
- `public/logo.svg`
- `public/README.md`
- `public/Orbitron-PRDkit.woff2`
- `src/App.css`
- `src/index.css`
- `src/main.tsx`
- `src/vite-env.d.ts`
- `src/components/DomPathBreadcrumb.css`
- `src/components/DomPathBreadcrumb.tsx`
- `src/components/Hotkey.css`
- `src/components/Hotkey.tsx`
- `src/utils/domUtils.ts`
- `src/utils/platform.ts`

## Manual merge targets

These files intentionally diverge in `viewer-publish/` and must be reviewed instead of blindly overwritten:

- `index.html`
- `package.json`
- `pnpm-lock.yaml`
- `tsconfig.json`
- `vite.config.ts`
- `src/App.tsx`
- `src/types.ts`
- `src/components/FileTree.css`
- `src/components/FileTree.tsx`
- `src/components/Header.css`
- `src/components/Header.tsx`
- `src/components/MarkPanel.css`
- `src/components/MarkPanel.tsx`
- `src/components/Preview.css`
- `src/components/Preview.tsx`

## Publish-only files

Never sync these from `viewer`:

- `viewer-publish/README.md`
- `viewer-publish/Dockerfile`
- `viewer-publish/docker-compose.yml`
- `viewer-publish/.dockerignore`
- `viewer-publish/scripts/serve.mjs`
- `viewer-publish/weblist/`
- any runtime artifact under `viewer-publish/dist/`
