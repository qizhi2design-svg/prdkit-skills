#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


MIRROR_FILES = [
    "public/favicon.svg",
    "public/logo.svg",
    "public/README.md",
    "public/Orbitron-PRDkit.woff2",
    "src/App.css",
    "src/index.css",
    "src/main.tsx",
    "src/vite-env.d.ts",
    "src/components/DomPathBreadcrumb.css",
    "src/components/DomPathBreadcrumb.tsx",
    "src/components/Hotkey.css",
    "src/components/Hotkey.tsx",
    "src/utils/domUtils.ts",
    "src/utils/platform.ts",
]

MANUAL_REVIEW_FILES = [
    "index.html",
    "package.json",
    "pnpm-lock.yaml",
    "tsconfig.json",
    "vite.config.ts",
    "src/App.tsx",
    "src/types.ts",
    "src/components/FileTree.css",
    "src/components/FileTree.tsx",
    "src/components/Header.css",
    "src/components/Header.tsx",
    "src/components/MarkPanel.css",
    "src/components/MarkPanel.tsx",
    "src/components/Preview.css",
    "src/components/Preview.tsx",
]


def repo_root() -> Path:
    env_root = Path.cwd()
    markers = [
        env_root / "cli" / "src" / "prototype" / "viewer",
        env_root / "viewer-publish",
    ]
    if all(path.exists() for path in markers):
        return env_root

    for base in [Path.cwd(), *Path(__file__).resolve().parents]:
        viewer_dir = base / "cli" / "src" / "prototype" / "viewer"
        publish_dir = base / "viewer-publish"
        if viewer_dir.exists() and publish_dir.exists():
            return base

    raise FileNotFoundError(
        "could not locate repo root containing both cli/src/prototype/viewer and viewer-publish"
    )


def run(cmd: list[str], cwd: Path) -> None:
    print(f"$ {' '.join(cmd)}")
    subprocess.run(cmd, cwd=cwd, check=True)


def copy_file(src_root: Path, dest_root: Path, rel_path: str, apply: bool) -> str:
    src = src_root / rel_path
    dest = dest_root / rel_path

    if not src.exists():
        raise FileNotFoundError(f"missing source file: {src}")

    if not apply:
        return f"would copy {rel_path}"

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    return f"copied {rel_path}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync shared files from cli/src/prototype/viewer to viewer-publish."
    )
    parser.add_argument("--apply", action="store_true", help="Apply file copies instead of dry-run.")
    parser.add_argument("--install", action="store_true", help="Run pnpm install in viewer-publish after sync.")
    parser.add_argument("--build", action="store_true", help="Run pnpm build in viewer-publish after sync.")
    args = parser.parse_args()

    try:
        root = repo_root()
    except FileNotFoundError as error:
        print(str(error), file=sys.stderr)
        return 1
    src_root = root / "cli" / "src" / "prototype" / "viewer"
    dest_root = root / "viewer-publish"

    if not src_root.exists():
        print(f"source viewer not found: {src_root}", file=sys.stderr)
        return 1

    if not dest_root.exists():
        print(f"publish viewer not found: {dest_root}", file=sys.stderr)
        return 1

    mode = "apply" if args.apply else "dry-run"
    print(f"sync mode: {mode}")
    print(f"source: {src_root}")
    print(f"target: {dest_root}")
    print("")

    for rel_path in MIRROR_FILES:
        print(copy_file(src_root, dest_root, rel_path, args.apply))

    print("")
    print("manual review required for:")
    for rel_path in MANUAL_REVIEW_FILES:
        print(f"- {rel_path}")

    if args.install:
        run(["pnpm", "install"], dest_root)

    if args.build:
        run(["pnpm", "build"], dest_root)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
