#!/usr/bin/env python3
"""Check app coefficients and release metadata against the companion JSON."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_embedded_model(index_path: Path) -> dict:
    source = index_path.read_text(encoding="utf-8")
    match = re.search(r"const studyData\s*=\s*(\{.*?\n\s*\});", source, re.S)
    if not match:
        raise ValueError(f"Could not locate embedded studyData in {index_path}")
    return json.loads(match.group(1))


def normalized_coefficients(model: dict) -> list[tuple[str, float]]:
    return [(item["id"], item["weight"]) for item in model["coefficients"]]


def check(app_root: Path, package_json: Path | None) -> list[str]:
    json_path = app_root / "data" / "study_data.json"
    model = json.loads(json_path.read_text(encoding="utf-8"))
    embedded = load_embedded_model(app_root / "index.html")
    cache_source = (app_root / "sw.js").read_text(encoding="utf-8")
    cache_match = re.search(r"CACHE_NAME\s*=\s*['\"]([^'\"]+)['\"]", cache_source)
    if not cache_match:
        raise ValueError(f"Could not locate CACHE_NAME in {app_root / 'sw.js'}")
    cache_name = cache_match.group(1)
    metadata = model["model_metadata"]
    embedded_metadata = embedded["model_metadata"]
    errors = []

    if normalized_coefficients(model) != normalized_coefficients(embedded):
        errors.append("Standalone JSON coefficient IDs or weights differ from embedded app coefficients.")
    for key in ("calibration_intercept", "app_release", "last_updated"):
        if metadata.get(key) != embedded_metadata.get(key):
            errors.append(f"Standalone JSON and embedded app metadata differ for {key}.")
    if metadata.get("app_release") != cache_name:
        errors.append("Standalone JSON app_release does not match the service-worker cache version.")
    if model.get("triage_thresholds") != embedded.get("triage_thresholds"):
        errors.append("Standalone JSON risk thresholds differ from embedded app thresholds.")
    for coefficient in model["coefficients"]:
        if "or" in coefficient and round(__import__("math").exp(coefficient["weight"]), 2) != coefficient["or"]:
            errors.append(f"Odds-ratio metadata for {coefficient['id']} is not exp(weight), rounded to 2 decimals.")

    compared = [("standalone JSON", json_path)]
    if package_json:
        packaged = json.loads(package_json.read_text(encoding="utf-8"))
        if packaged != model:
            errors.append("Packaged JSON content differs from the current standalone JSON.")
        compared.append(("packaged JSON", package_json))

    for label, path in compared:
        print(f"{label} SHA-256: {sha256(path)}")
    print(f"App release/cache: {metadata.get('app_release')} / {cache_name}")
    print(f"Coefficient entries: {len(model['coefficients'])}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package-json", type=Path, help="Optional JSON copied into a publication package")
    args = parser.parse_args()
    app_root = Path(__file__).resolve().parents[1]
    try:
        errors = check(app_root, args.package_json)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print("PASS: embedded app, standalone JSON, release cache, and optional package JSON are synchronized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
