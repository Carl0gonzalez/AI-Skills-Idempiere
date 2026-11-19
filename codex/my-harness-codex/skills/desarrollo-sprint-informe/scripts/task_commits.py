#!/usr/bin/env python3
"""Read local ticket references, including linked worktrees; never claim deployment."""
import argparse
import json
from pathlib import Path
import re
import subprocess


def git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def discover(workspace=None, repos=()):
    candidates = list(map(Path, repos))
    if workspace:
        root = Path(workspace)
        if not root.is_dir():
            raise ValueError("Workspace directory does not exist")
        if (root / ".git").exists():
            candidates.append(root)
        candidates.extend(p for p in root.iterdir() if p.is_dir() and (p / ".git").exists())
    found = []
    for path in candidates:
        top = Path(git(path, "rev-parse", "--show-toplevel")).resolve()
        if top not in found:
            found.append(top)
    return sorted(found)


def scan(repo, task, release_refs):
    pattern = re.compile(r"(?<![A-Za-z0-9])" + re.escape(task) + r"(?![A-Za-z0-9])", re.I)
    candidate_shas = git(repo, "log", "--all", "--no-merges", "--fixed-strings",
                         "--regexp-ignore-case", "--grep=" + task, "--format=%H").splitlines()
    refs = {}
    for ref in release_refs:
        try:
            refs[ref] = git(repo, "rev-parse", "--verify", "--end-of-options", ref + "^{commit}")
        except subprocess.CalledProcessError:
            refs[ref] = None
    commits = []
    for sha in candidate_shas:
        message = git(repo, "show", "-s", "--format=%s%x00%B", sha)
        subject, _, body = message.partition("\x00")
        if not pattern.search(body):
            continue
        containing = []
        for ref, ref_sha in refs.items():
            if ref_sha is None:
                continue
            code = subprocess.run(["git", "-C", str(repo), "merge-base", "--is-ancestor",
                                   sha, ref_sha], capture_output=True).returncode
            if code not in (0, 1):
                raise RuntimeError("Cannot check commit ancestry")
            if code == 0:
                containing.append(ref)
        commits.append({"sha": sha, "subject": subject, "contained_in_refs": containing})
    branches = [b for b in git(repo, "for-each-ref", "--format=%(refname:short)",
                              "refs/heads", "refs/remotes").splitlines() if pattern.search(b)]
    summaries = [{"ref": ref, "sha": sha,
                  "all_matching_commits_contained":
                  all(ref in c["contained_in_refs"] for c in commits) if commits and sha else None}
                 for ref, sha in refs.items()]
    return {"repo": str(repo), "task": task, "commits": commits, "branches": branches,
            "release_refs": summaries, "deployment": "not_verified",
            "status": "references_found" if commits or branches else "no_references_found"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace")
    parser.add_argument("--repo", action="append", default=[])
    parser.add_argument("--release-ref", action="append", default=[])
    parser.add_argument("tickets", nargs="+")
    args = parser.parse_args()
    if not args.workspace and not args.repo:
        parser.error("Provide --workspace or --repo")
    try:
        repos = discover(args.workspace, args.repo)
        records = [scan(repo, task, args.release_ref) for task in args.tickets for repo in repos]
        print(json.dumps({"scope": "local_refs_only", "repos_examined": list(map(str, repos)),
                          "records": records}, ensure_ascii=False, indent=2))
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        parser.exit(2, "Scan incomplete: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
