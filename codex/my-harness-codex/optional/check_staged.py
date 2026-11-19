#!/usr/bin/env python3
"""Optional manual staged syntax check; does not install or modify Git hooks."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile


def check(repo):
    names = subprocess.run(["git", "-C", str(repo), "diff", "--cached", "--name-only",
                            "--diff-filter=ACMRT", "-z"], capture_output=True, check=True).stdout
    results = []
    for raw in names.split(b"\0"):
        if not raw:
            continue
        name = raw.decode("utf-8", errors="surrogateescape")
        # Inspect the index blob, including partially staged and symlink entries.
        blob = subprocess.run(["git", "-C", str(repo), "show", ":" + name],
                              capture_output=True, check=True).stdout
        suffix = Path(name).suffix.lower()
        if suffix not in (".py", ".json", ".yaml", ".yml", ".sh", ".bash"):
            continue
        result = {"path": name, "status": "PASA", "source": "index_blob"}
        try:
            if suffix == ".py":
                compile(blob, name, "exec", dont_inherit=True)
            elif suffix == ".json":
                json.loads(blob)
            elif suffix in (".yaml", ".yml"):
                try:
                    import yaml
                except ImportError:
                    result.update(status="NO EJECUTADO", reason="PyYAML unavailable")
                else:
                    list(yaml.safe_load_all(blob))
            else:
                with tempfile.TemporaryFile() as stream:
                    stream.write(blob)
                    stream.seek(0)
                    proc = subprocess.run(["bash", "-n"], stdin=stream, capture_output=True)
                if proc.returncode:
                    raise ValueError(proc.stderr.decode(errors="replace").strip())
        except (SyntaxError, ValueError, UnicodeError) as exc:
            result.update(status="FALLA", reason=str(exc))
        except Exception as exc:
            # Includes YAML parser failures; report tool failure separately.
            if suffix in (".yaml", ".yml") and type(exc).__module__.startswith("yaml"):
                result.update(status="FALLA", reason=str(exc))
            else:
                result.update(status="NO EJECUTADO", reason=str(exc))
        results.append(result)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    try:
        results = check(args.repo)
    except (OSError, subprocess.CalledProcessError) as exc:
        parser.exit(2, "Cannot read index: " + str(exc) + "\n")
    print(json.dumps(results, ensure_ascii=True, indent=2))
    if any(r["status"] == "FALLA" for r in results):
        return 1
    if any(r["status"] == "NO EJECUTADO" for r in results):
        return 2
    return 0 if results else 2


if __name__ == "__main__":
    raise SystemExit(main())
