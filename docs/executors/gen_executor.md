# GEN executor contract

The GEN phase can be delegated to an external executor without changing Control Kernel
or OPA gating semantics. The executor interface is explicit and schema-validated.

## Contract schema

* Schema: `control/executors/gen_executor.schema.json`
* Definitions:
  * `config`: executor configuration (local or external).
  * `request`: input bundle for the executor.
  * `report`: execution report emitted by the executor.

The runner validates the request and report against the schema definitions before
continuing the pipeline.

## Configuration

Select an executor explicitly via:

1. `CBIA_GEN_EXECUTOR_CONFIG=/path/to/gen_executor.json`, or
2. `control/runtime/gen_executor.json`.

When neither is configured, the built-in GEN behavior remains the default.

### Configuration fields

The configuration is validated against the `config` schema definition.

Required:

* `kind`: `local` or `external`.
* `version`: executor version string.

`external` requires:

* `command`: argument vector to invoke (e.g., `["/usr/bin/python3", "tools/executors/gen_local.py"]`).
* Optional `timeout_s` and `env` can further constrain execution.

`local` uses the built-in GEN behavior unless a `command` is supplied.

## Request (inputs)

The runner writes a JSON request containing:

* `pre_gen_capsule`: admission context from `control/runtime/pre_gen_capsule.json`.
* `inputs_manifest`: resolved inputs manifest payload.
* `phase_config`: GEN configuration including output paths.

## Report (outputs)

The executor writes a JSON report containing:

* `artifacts`: list of produced artifacts with hashes and byte counts.
* `tool_versions`: executor tool/version identifiers.

Artifacts must be written to the paths declared in `phase_config.outputs`.

### Configuration file fields

Example:

```json
{
  "kind": "external",
  "version": "local-0.1.0",
  "command": ["/usr/bin/python3", "tools/executors/gen_local.py"],
  "phase_config": {
    "phase": "GEN",
    "outputs": {
      "outputs_manifest": "execution/gen/outputs.json",
      "execution_report": "execution/gen/executor.report.json"
    }
  }
}
```
