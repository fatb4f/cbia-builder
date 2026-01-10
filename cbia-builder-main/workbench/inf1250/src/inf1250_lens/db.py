"""
REFERENCE ONLY — NOT EXECUTED

This file is a reference mirror of the GPT-executed Generative Execution DAG (GED).
It MUST NOT be invoked as a controller or execution entrypoint.
"""

"""DuckDB execution and observability helpers (stub)."""
def duckdb_connect(path="data/inf1250.duckdb"):
    raise NotImplementedError

def run_sql(conn, sql, params=None):
    raise NotImplementedError

def explain(conn, sql):
    raise NotImplementedError

def assert_rows(conn, sql, *, min=None, max=None, equals=None):
    raise NotImplementedError
