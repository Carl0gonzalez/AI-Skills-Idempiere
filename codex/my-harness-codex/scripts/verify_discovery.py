#!/usr/bin/env python3
"""Ask the installed Codex app-server to reload personal skills; no model turn."""
import json
from pathlib import Path
import selectors
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def verify():
    proc = subprocess.Popen(["codex", "app-server", "--stdio", "--disable", "apps",
                             "--disable", "plugins", "-c", "analytics.enabled=false"],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, text=True, bufsize=1)
    selector = selectors.DefaultSelector()
    selector.register(proc.stdout, selectors.EVENT_READ)

    def send(message):
        proc.stdin.write(json.dumps(message) + "\n")
        proc.stdin.flush()

    def receive(request_id):
        deadline = time.monotonic() + 25
        while time.monotonic() < deadline:
            if not selector.select(timeout=1):
                if proc.poll() is not None:
                    raise RuntimeError("Codex app-server exited before responding")
                continue
            line = proc.stdout.readline()
            if not line:
                raise RuntimeError("Codex app-server closed stdout")
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                continue
            if message.get("id") == request_id:
                if "error" in message:
                    raise RuntimeError("App-server error: " + str(message["error"]))
                return message["result"]
        raise TimeoutError("Local discovery did not respond within 25 seconds")

    try:
        send({"id": 1, "method": "initialize", "params": {
            "clientInfo": {"name": "harness-local-validation", "version": "1.0"},
            "capabilities": {"experimentalApi": True}}})
        receive(1)
        send({"method": "initialized", "params": {}})
        send({"id": 2, "method": "skills/list", "params": {
            "cwds": [str(ROOT.parent)], "forceReload": True}})
        result = receive(2)
        expected = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        skills = [s for entry in result["data"] for s in entry["skills"] if s["name"] in expected]
        errors = [e for entry in result["data"] for e in entry["errors"]
                  if "my-harness-codex" in e["path"] or "desarrollo-" in e["path"]]
        report = {"method": "skills/list", "model_turns": 0,
                  "skills": [{k: s[k] for k in ("name", "enabled", "path", "scope")} for s in skills],
                  "errors": errors,
                  "missing": sorted(expected - {s["name"] for s in skills}),
                  "disabled": sorted({s["name"] for s in skills if not s["enabled"]})}
        return report
    finally:
        selector.close()
        proc.terminate()
        try:
            proc.wait(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()


if __name__ == "__main__":
    try:
        report = verify()
    except (OSError, RuntimeError, TimeoutError, KeyError) as exc:
        raise SystemExit("Local discovery unavailable: " + str(exc)) from None
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(bool(report["errors"] or report["missing"] or report["disabled"]))
