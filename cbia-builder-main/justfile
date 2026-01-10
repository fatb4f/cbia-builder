set dotenv-load := true

sync:
  uv sync --all-extras

projects:
  uv run python scripts/list_projects.py

validate-schemas PROJECT:
  uv run python scripts/validate_schemas.py --project {{PROJECT}}

check-material PROJECT:
  uv run python scripts/check_material.py --project {{PROJECT}}

update-stage PROJECT STAGE:
  uv run python scripts/update_stage.py --project {{PROJECT}} --stage {{STAGE}}
