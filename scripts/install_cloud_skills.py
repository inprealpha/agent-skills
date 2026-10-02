#!/usr/bin/env python3
"""Copy this bundle's skills into a project, without replacing existing skills."""

import argparse
from pathlib import Path
import shutil


def tree_contents(directory):
    if directory.is_symlink() or not directory.is_dir():
        raise ValueError(f"Expected a real directory: {directory}")
    result = {}
    for path in directory.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not supported: {path}")
        if path.is_file():
            result[path.relative_to(directory)] = path.read_bytes()
    return result


def install(source, project):
    project = project.resolve(strict=True)
    if not project.is_dir():
        raise ValueError(f"Expected a project directory: {project}")
    destination = project / ".agents" / "skills"
    for parent in (project / ".agents", destination):
        if parent.is_symlink() or (parent.exists() and not parent.is_dir()):
            raise ValueError(f"Expected a real directory: {parent}")
    skills = sorted(path.parent for path in source.glob("*/SKILL.md"))
    if not skills:
        raise ValueError(f"No skills found in {source}")
    pending = []
    # Check every conflict before copying anything.
    for skill in skills:
        contents = tree_contents(skill)
        target = destination / skill.name
        if target.exists() or target.is_symlink():
            if tree_contents(target) != contents:
                raise ValueError(f"Existing skill differs; no skills were installed: {target}")
        else:
            pending.append((skill, target))
    destination.mkdir(parents=True, exist_ok=True)
    for skill, target in pending:
        shutil.copytree(skill, target)
    return len(pending), len(skills), destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path, help="Existing project root")
    args = parser.parse_args()
    try:
        added, total, destination = install(Path(__file__).resolve().parents[1] / "skills", args.project)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(f"Installed {added} skills; {total} skills available in {destination}")
    print("Start a new Codex task in this project to discover the skills.")


if __name__ == "__main__":
    main()
