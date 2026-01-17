#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import jsonschema


@dataclass(frozen=True)
class CheckResult:
    contract_id: str
    ok: bool
    reasons: list[str]
    matched_forbidden: list[str]
    matched_deprecated: list[str]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON at {path}: {exc}") from exc


def validate_contract(contract: dict[str, Any], schema_path: Path) -> None:
    schema = load_json(schema_path)
    jsonschema.validate(instance=contract, schema=schema)


def to_rel_path(root: Path, path: Path) -> str:
    return path.resolve().relative_to(root).as_posix()


def glob_matches(root: Path, patterns: Iterable[str]) -> list[str]:
    matches: set[str] = set()
    for pattern in patterns:
        for found in glob.glob(str(root / pattern), recursive=True):
            candidate = Path(found)
            if candidate.exists():
                matches.add(to_rel_path(root, candidate))
    return sorted(matches)


def filter_matches_by_scopes(
    root: Path,
    matches: Iterable[str],
    scopes: Iterable[Path],
) -> list[str]:
    scope_paths = []
    for scope in scopes:
        if scope.exists():
            scope_paths.append(to_rel_path(root, scope))

    filtered: set[str] = set()
    for match in matches:
        for scope in scope_paths:
            if match == scope or match.startswith(f"{scope}/"):
                filtered.add(match)
                break
    return sorted(filtered)


def exact_matches(root: Path, paths: Iterable[str]) -> list[str]:
    matches: list[str] = []
    for rel in paths:
        candidate = root / rel
        if candidate.exists():
            matches.append(rel)
    return sorted(set(matches))


def check_allowed_roots(root: Path, allowed_roots: Iterable[str], reasons: list[str]) -> None:
    for allowed in allowed_roots:
        if not (root / allowed).exists():
            reasons.append(f"Allowed root missing: {allowed}")


def check_builder_snapshot(root: Path, snapshot: dict[str, Any], reasons: list[str]) -> None:
    snapshot_root = root / snapshot["root"]
    if not snapshot_root.exists():
        reasons.append(f"Builder snapshot root missing: {snapshot['root']}")
        return
    for required in snapshot.get("required_paths", []):
        if not (snapshot_root / required).exists():
            reasons.append(f"Builder snapshot missing path: {snapshot['root']}/{required}")


def check_consumer_view(root: Path, consumer_view: dict[str, Any], reasons: list[str]) -> None:
    manifest = root / consumer_view["manifest_path"]
    if not manifest.exists():
        reasons.append(f"Consumer manifest missing: {consumer_view['manifest_path']}")
    material_root = root / consumer_view["material_root"]
    if not material_root.exists():
        reasons.append(f"Consumer material root missing: {consumer_view['material_root']}")


def emit_evidence(evidence_path: Path, result: CheckResult) -> None:
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "contract_id": result.contract_id,
        "ok": result.ok,
        "reasons": result.reasons,
        "matched_forbidden": result.matched_forbidden,
        "matched_deprecated": result.matched_deprecated,
        "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
    }
    evidence_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def run_check(
    root: Path,
    contract_path: Path,
    schema_path: Path,
    deprecations_path: Path,
) -> CheckResult:
    contract = load_json(contract_path)
    validate_contract(contract, schema_path)
    deprecations = load_json(deprecations_path)

    reasons: list[str] = []
    check_allowed_roots(root, contract["allowed_roots"], reasons)
    check_builder_snapshot(root, contract["builder_snapshot"], reasons)
    check_consumer_view(root, contract["consumer_view"], reasons)

    builder_root = root / contract["builder_snapshot"]["root"]
    required_paths = contract["builder_snapshot"].get("required_paths", [])
    forbidden_scopes = [builder_root / path for path in required_paths]
    forbidden_scopes.append(root / contract["consumer_view"]["material_root"])

    matched_forbidden = filter_matches_by_scopes(
        root,
        glob_matches(root, contract.get("forbidden_globs", [])),
        forbidden_scopes,
    )
    if matched_forbidden:
        reasons.append(f"Forbidden glob matches: {len(matched_forbidden)}")

    deprecation_scopes = [root / "dist", root / "build"]
    deprecation_scopes.extend(builder_root / path for path in required_paths)
    deprecation_scopes.append(root / contract["consumer_view"]["material_root"])

    matched_deprecated = filter_matches_by_scopes(
        root,
        glob_matches(root, deprecations.get("deny_globs", [])),
        deprecation_scopes,
    )
    matched_deprecated += exact_matches(root, deprecations.get("deny_paths", []))
    matched_deprecated = sorted(set(matched_deprecated))
    if matched_deprecated:
        reasons.append(f"Deprecated outputs matched: {len(matched_deprecated)}")

    ok = not reasons
    return CheckResult(
        contract_id=contract["contract_id"],
        ok=ok,
        reasons=reasons,
        matched_forbidden=matched_forbidden,
        matched_deprecated=matched_deprecated,
    )


def render_dag_mermaid(dag_json_path: Path, output_path: Path) -> None:
    dag = load_json(dag_json_path)
    nodes = dag.get("nodes", [])
    edges = dag.get("edges", [])

    lines = [
        "%% Generated by tools/verify_repo_mode_b.py --render-dag-mermaid",
        "flowchart TD",
    ]

    for node in nodes:
        node_id = node["id"]
        node_type = node.get("type", "step")
        if node_type == "terminal":
            lines.append(f"    {node_id}([\"{node_id}\"])")
        else:
            lines.append(f"    {node_id}[\"{node_id}\"]")

    for edge in edges:
        condition = edge.get("condition")
        if condition:
            lines.append(f"    {edge['from']} -->|{condition}| {edge['to']}")
        else:
            lines.append(f"    {edge['from']} --> {edge['to']}")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify repo Mode B contract.")
    parser.add_argument("--root", type=Path, default=repo_root())
    parser.add_argument(
        "--contract",
        type=Path,
        default=Path("control/contracts/repo_mode_b.contract.json"),
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("control/contracts/repo_mode_b.contract.schema.json"),
    )
    parser.add_argument(
        "--deprecations",
        type=Path,
        default=Path("control/deprecations/deprecated_outputs.json"),
    )
    parser.add_argument(
        "--render-dag-mermaid",
        action="store_true",
        help="Render Mermaid view from control/plant/repo_mode_b_dag.json.",
    )
    parser.add_argument(
        "--dag-json",
        type=Path,
        default=Path("control/plant/repo_mode_b_dag.json"),
    )
    parser.add_argument(
        "--dag-mmd",
        type=Path,
        default=Path("control/plant/repo_mode_b_dag.mmd"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.resolve()

    if args.render_dag_mermaid:
        render_dag_mermaid(root / args.dag_json, root / args.dag_mmd)
        print(f"Wrote Mermaid DAG to {args.dag_mmd}")
        return 0

    try:
        contract_path = root / args.contract
        schema_path = root / args.schema
        deprecations_path = root / args.deprecations
        result = run_check(root, contract_path, schema_path, deprecations_path)
        contract = load_json(contract_path)
        evidence_path = root / contract["evidence_outputs"]["repo_mode_b_check"]
        emit_evidence(evidence_path, result)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if result.ok:
        print("ALLOW")
        return 0

    print("DENY")
    for reason in result.reasons:
        print(f"- {reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
