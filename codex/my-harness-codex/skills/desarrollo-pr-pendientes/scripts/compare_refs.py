#!/usr/bin/env python3
"""Compare endpoint trees without interpreting history as deployment evidence."""
import argparse
import json
import subprocess


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def compare(repo, target, source, paths):
    target_sha = git(repo, "rev-parse", "--verify", "--end-of-options", target + "^{commit}")
    source_sha = git(repo, "rev-parse", "--verify", "--end-of-options", source + "^{commit}")
    result = subprocess.run(["git", "-C", str(repo), "--literal-pathspecs", "diff",
                             "--quiet", "--no-ext-diff", "--no-textconv", target_sha,
                             source_sha, "--", *paths], capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip())
    return {"target": target, "source": source, "target_sha": target_sha,
            "source_sha": source_sha, "paths": paths, "same_content": result.returncode == 0,
            "interpretation": "same_endpoint_content" if result.returncode == 0 else
            "different_content_review_required", "deployment": "not_verified",
            "scope": "selected_paths" if paths else "whole_tree"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    try:
        print(json.dumps(compare(args.repo, args.target, args.source, args.paths), ensure_ascii=False))
    except (OSError, subprocess.CalledProcessError, RuntimeError) as exc:
        parser.exit(2, "Comparison unavailable: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
