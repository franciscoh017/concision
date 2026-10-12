#!/usr/bin/env python3
"""Check the skill entrypoint, references, and distribution metadata."""

import json
from pathlib import Path
import re
import sys

import yaml


def check(condition, message):
    if not condition:
        raise ValueError(message)


def validate(root):
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---", 2)
    check(len(parts) == 3 and not parts[0].strip(), "SKILL.md needs YAML frontmatter")
    skill = yaml.safe_load(parts[1])
    check(isinstance(skill, dict), "Skill frontmatter must be a mapping")
    name = skill.get("name", "")
    check(isinstance(name, str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
          and len(name) <= 64, "Invalid skill name")
    check(name == "concision", "The distributed skill must be named concision")
    description = skill.get("description", "")
    check(isinstance(description, str) and 1 <= len(description) <= 1024,
          "Description must contain 1–1024 characters")
    metadata = skill.get("metadata", {})
    check(isinstance(metadata, dict) and all(isinstance(v, str) for v in metadata.values()),
          "Skill metadata values must be strings")
    version = metadata.get("version", "")
    check(re.fullmatch(r"\d+\.\d+\.\d+", version), "Use a semantic version in metadata.version")
    check(skill.get("license") == "MIT", "Skill license must be MIT")
    check("MIT License" in (root / "LICENSE").read_text(), "Missing MIT license text")

    manifests = [json.loads((root / path).read_text()) for path in (
        ".claude-plugin/plugin.json", ".cursor-plugin/plugin.json")]
    summary = description.split(". ", 1)[0] + "."
    for manifest in manifests:
        check(manifest.get("name") == name, "Plugin name differs from skill name")
        check(manifest.get("version") == version, "Plugin version differs from skill version")
        check(manifest.get("license") == "MIT", "Plugin license differs from skill license")
        check(manifest.get("description") == summary, "Plugin description differs from skill summary")
        check(manifest.get("repository") == "https://github.com/franciscoh017/concision",
              "Plugin repository URL is incorrect")
    check(manifests[0].get("skills") == ["./"], "Claude plugin must load the root skill")
    check("skills" not in manifests[1], "Cursor plugin must use root skill discovery")
    marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    check(marketplace.get("name") == name, "Marketplace name differs from skill name")
    entries = marketplace.get("plugins", [])
    check(len(entries) == 1 and entries[0].get("name") == name
          and entries[0].get("source") == "./", "Marketplace must install the root plugin")
    check(entries[0].get("license") == "MIT" and entries[0].get("description") == summary,
          "Marketplace metadata differs from the skill")

    interface = yaml.safe_load((root / "agents/openai.yaml").read_text())["interface"]
    check(25 <= len(interface["short_description"]) <= 64, "Invalid interface description length")
    check(f"${name}" in interface["default_prompt"], "Default prompt must invoke the skill")
    changelog = (root / "CHANGELOG.md").read_text()
    latest = re.search(r"^## ([0-9.]+) -", changelog, re.M)
    check(latest and latest.group(1) == version, "Newest changelog version differs from skill version")
    check(f"npx skills add franciscoh017/{name}" in (root / "README.md").read_text(),
          "README must include the Skills CLI install command")
    for path in [root / "README.md", root / "SKILL.md", *root.glob("references/*.md")]:
        for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text()):
            if ":" not in target and not target.startswith("#"):
                check((path.parent / target.split("#", 1)[0]).exists(),
                      f"Broken local link in {path.name}: {target}")
    print(f"Concision {version}: package metadata and local links are valid.")


if __name__ == "__main__":
    try:
        validate(Path(__file__).resolve().parents[1])
    except (ValueError, KeyError, TypeError, AttributeError, OSError, yaml.YAMLError) as error:
        sys.exit(f"Package validation failed: {error}")
