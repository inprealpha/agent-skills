#!/usr/bin/env python3
"""Validate the plugin and optionally build a ZIP. Requires PyYAML for validation."""

import argparse
import json
from pathlib import Path
import re
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate():
    manifest = json.loads((ROOT / "plugin.json").read_text())
    compatibility = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    for key in ("name", "version", "description", "author", "repository"):
        assert manifest[key] == compatibility[key], f"Manifest mismatch: {key}"
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest["name"])
    assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])
    assert compatibility["skills"] == "./skills/"
    assert compatibility["interface"] == manifest["extensions"]["com.openai"]["interface"]
    marketplace = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
    entry, = marketplace["plugins"]
    assert entry["name"] == manifest["name"]
    assert entry["source"] == {"source": "local", "path": "./"}
    assert entry["policy"] == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}
    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    assert skill_files, "No skills found"
    names = set()
    for path in skill_files:
        content = path.read_text()
        match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
        assert match, f"Missing frontmatter: {path}"
        metadata = yaml.safe_load(match.group(1))
        name = metadata["name"]
        assert name == path.parent.name and name not in names, f"Invalid or duplicate name: {path}"
        names.add(name)
        assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) and len(name) <= 64
        assert isinstance(metadata["description"], str) and 0 < len(metadata["description"]) <= 1024
        if metadata.get("disable-model-invocation"):
            policy = yaml.safe_load((path.parent / "agents/openai.yaml").read_text())
            assert policy["policy"]["allow_implicit_invocation"] is False, f"Invocation policy lost: {path}"
        # Only check local Markdown links; web links and fenced examples are excluded.
        body = re.sub(r"```.*?```", "", content[match.end():], flags=re.DOTALL)
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            if "://" not in link and not link.startswith("#"):
                target = (path.parent / link.split("#")[0]).resolve()
                assert target.is_relative_to(ROOT) and target.exists(), f"Broken link: {path}: {link}"
    for path in (ROOT / "skills").rglob("*"):
        assert not path.is_symlink(), f"Nonportable symlink: {path}"
    print(f"Validated {manifest['name']} {manifest['version']}: {len(skill_files)} skills")
    return manifest


def build(output):
    files = [ROOT / "plugin.json", ROOT / ".codex-plugin/plugin.json", ROOT / "README.md"]
    files += sorted(path for path in (ROOT / "skills").rglob("*") if path.is_file())
    files.append(ROOT / "scripts/install_cloud_skills.py")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    print(f"Built {output} ({len(files)} files)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Build a ZIP at this path after validation")
    args = parser.parse_args()
    validate()
    if args.output:
        build(args.output)


if __name__ == "__main__":
    main()
