# Deterministic cache

## Cache key components
The cache key is a SHA-256 hash of the canonical JSON encoding of the cache key data,
which must conform to `execution/cache/cache_key.schema.json`.

Required components:
- `authority_ledger_hash`: SHA-256 of `control/authority.ledger.json`.
- `policy_bundle_hash`: SHA-256 of the `policy/` bundle as recorded in the pre-gen capsule.
- `pre_gen_capsule_hash`: SHA-256 of `control/runtime/pre_gen_capsule.json`.
- `inputs_manifest_hash`: SHA-256 of `execution/ledger/inputs.manifest.json` (empty string if absent).
- `phase`: Pipeline phase identifier (GEN/CHECK/REPAIR/PROMOTE).
- `tool_versions`: Versions that affect outputs (`runner_version`, `generator_version`).

## Stability rules
- Canonical JSON encoding is UTF-8, sorted keys, and no extra whitespace.
- No timestamps, UUIDs, or environment-dependent ordering are permitted in cache key data.
- Cache keys must be computed after Control Kernel admission.
- Cache hits must still emit OPA decision/explain artifacts and ledger evidence.

## On-disk layout
```
execution/cache/<cache_key>/
  cache.meta.json
  execution/gen/outputs.json
  opa/decision.json
  opa/explain.json
  opa/bundle.hash
```

`cache.meta.json` records the cache key data, cached artifacts, and phase artifacts.
