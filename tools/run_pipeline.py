#!/usr/bin/env python3
import json, os, hashlib, subprocess, sys, datetime

ROOT = os.path.dirname(os.path.dirname(__file__))

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(8192), b""):
            h.update(b)
    return h.hexdigest()

def load(p):
    with open(p) as f:
        return json.load(f)

def save(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        json.dump(obj, f, indent=2)

def pre_gen():
    auth = load(os.path.join(ROOT, "control/authority.ledger.json"))
    hashes = {a["authority_id"]: a["hash"]["value"] for a in auth["authority_set"]}
    capsule = {
        "schema_version": "0.1.0",
        "kernel_decision": "ALLOW" if auth.get("frozen") else "DENY",
        "control_state_hash": hashlib.sha256(json.dumps(hashes, sort_keys=True).encode()).hexdigest(),
        "policy_bundle_hash": "local-dev",
        "authority_set_hashes": hashes,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }
    save(os.path.join(ROOT, "control/runtime/pre_gen_capsule.json"), capsule)
    if capsule["kernel_decision"] != "ALLOW":
        sys.exit("PRE-GEN denied")

def opa_gate():
    input_bundle = {
        "pre_gen_capsule": load(os.path.join(ROOT, "control/runtime/pre_gen_capsule.json")),
        "authority_ledger": load(os.path.join(ROOT, "control/authority.ledger.json")),
        "objectives": load(os.path.join(ROOT, "objectives.json")) if os.path.exists(os.path.join(ROOT, "objectives.json")) else [],
        "dependency_graph": load(os.path.join(ROOT, "dependency.graph.json")) if os.path.exists(os.path.join(ROOT, "dependency.graph.json")) else {},
        "execution_dag": load(os.path.join(ROOT, "execution_dag.json")) if os.path.exists(os.path.join(ROOT, "execution_dag.json")) else {},
        "run_ledger": load(os.path.join(ROOT, "execution/ledger/run.ledger.json")) if os.path.exists(os.path.join(ROOT, "execution/ledger/run.ledger.json")) else [],
        "artifact_hashes": load(os.path.join(ROOT, "execution/ledger/artifact_hashes.json")) if os.path.exists(os.path.join(ROOT, "execution/ledger/artifact_hashes.json")) else {}
    }
    save(os.path.join(ROOT, "opa/input.json"), input_bundle)
    # assumes `opa` binary available
    subprocess.check_call([
        "opa","eval","-d",os.path.join(ROOT,"policy"),
        "-i",os.path.join(ROOT,"opa/input.json"),
        "data.assurance.allow","--format","json","--explain","full"
    ], stdout=open(os.path.join(ROOT,"opa/decision.json"),"w"))
    # naive allow check
    with open(os.path.join(ROOT,"opa/decision.json")) as f:
        if ""true"" not in f.read():
            sys.exit("OPA gate denied")

def gen_dummy():
    os.makedirs(os.path.join(ROOT,"artifacts"), exist_ok=True)
    path = os.path.join(ROOT,"artifacts","dummy.txt")
    with open(path,"w") as f:
        f.write("content")
    h = sha256(path)
    ledger = [{
        "entry_id": "RUN-0001",
        "phase": "GEN",
        "artifact_id": "dummy",
        "artifact_path": "artifacts/dummy.txt",
        "hash": h,
        "objective_ids": [],
        "authority_ids": [],
        "policy_bundle_hash": "local-dev"
    }]
    save(os.path.join(ROOT,"execution/ledger/run.ledger.json"), ledger)
    save(os.path.join(ROOT,"execution/ledger/artifact_hashes.json"), { "artifacts/dummy.txt": h })

def main():
    pre_gen()
    opa_gate()
    gen_dummy()
    print("Pipeline completed")

if __name__ == "__main__":
    main()