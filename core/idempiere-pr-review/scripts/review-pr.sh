#!/usr/bin/env bash
# Original local adaptation: isolated, unpublished PR integration review.
set -euo pipefail
usage() {
  echo 'Usage: review-pr.sh prepare <PR> <absolute-new-worktree-path> [upstream]'
  echo '       review-pr.sh cleanup <absolute-worktree-path>'
}
fail() { echo "$1" >&2; exit 1; }
absolute_path() {
  [[ "$1" = /* && "$1" != *$'\n'* && "$1" != *$'\t'* ]] || fail 'Use an absolute path without tabs/newlines.'
}
[[ "${1:-}" != --help && "${1:-}" != -h ]] || { usage; exit 0; }
mode=${1:-}
case "$mode" in
prepare)
  [[ $# -ge 3 && $# -le 4 && "$2" =~ ^[1-9][0-9]*$ ]] || { usage; exit 1; }
  pr=$2; destination=$3; remote=${4:-upstream}
  absolute_path "$destination"
  [[ "$remote" =~ ^[a-zA-Z0-9_-]+$ ]] || fail 'Invalid remote name.'
  [[ ! -e "$destination" && ! -L "$destination" ]] || fail 'Destination already exists; nothing was overwritten.'
  root=$(git rev-parse --show-toplevel)
  # Never switch/stash/reset this checkout, including its untracked work.
  remote_url=$(git -C "$root" remote get-url "$remote")
  case "$remote_url" in
    https://github.com/idempiere/idempiere|https://github.com/idempiere/idempiere.git|git@github.com:idempiere/idempiere.git|ssh://git@github.com/idempiere/idempiere.git) ;;
    *) fail 'Remote is not the official iDempiere upstream; its URL was not printed.' ;;
  esac
  review_ref="refs/idempiere-review/$$-$pr"
  created=false
  committed=false
  cleanup_prepare() {
    if $created && ! $committed; then
      git -C "$destination" merge --abort >/dev/null 2>&1 || true
      git -C "$root" worktree remove "$destination" >/dev/null 2>&1 || true
    fi
    git -C "$root" update-ref -d "$review_ref/base" >/dev/null 2>&1 || true
    git -C "$root" update-ref -d "$review_ref/pr" >/dev/null 2>&1 || true
  }
  trap cleanup_prepare EXIT
  # Avoid printing transport errors that could contain credential-bearing rewrites.
  if ! git -C "$root" fetch --quiet "$remote" "refs/heads/master:$review_ref/base" "refs/pull/$pr/head:$review_ref/pr" >/dev/null 2>&1; then
    fail 'Fetch failed; inspect transport configuration privately. No worktree was created.'
  fi
  base=$(git -C "$root" rev-parse "$review_ref/base")
  head=$(git -C "$root" rev-parse "$review_ref/pr")
  git -C "$root" worktree add --quiet --detach "$destination" "$base"
  created=true
  if ! git -C "$destination" -c core.hooksPath=/dev/null -c commit.gpgSign=false merge --quiet --no-ff --no-edit -m "Local review of PR #$pr (do not publish)" "$head" >/dev/null 2>&1; then
    fail 'Local integration merge failed; original checkout is unchanged. Check merge compatibility and local Git identity.'
  fi
  destination=$(git -C "$destination" rev-parse --show-toplevel)
  integrated=$(git -C "$destination" rev-parse HEAD)
  gitdir=$(git -C "$destination" rev-parse --absolute-git-dir)
  [[ ! -e "$gitdir/idempiere-review-state" ]] || fail 'Review metadata already exists.'
  printf '%s\n%s\n%s\n%s\n%s\n' "$destination" "$integrated" "$base" "$head" "$pr" > "$gitdir/idempiere-review-state"
  committed=true
  echo "Prepared PR #$pr at $destination"
  echo "Base: $base"
  echo "PR head: $head"
  echo "Integrated HEAD: $integrated (local review only)"
  git -C "$destination" diff --stat "$base" HEAD
  echo 'No database migration, build, server or publication was executed.'
  ;;
cleanup)
  [[ $# -eq 2 ]] || { usage; exit 1; }
  destination=$2; absolute_path "$destination"
  destination=$(git -C "$destination" rev-parse --show-toplevel)
  gitdir=$(git -C "$destination" rev-parse --absolute-git-dir)
  state="$gitdir/idempiere-review-state"
  [[ -f "$state" ]] || fail 'Not a worktree prepared by this helper; cleanup refused.'
  metadata=()
  while IFS= read -r line; do metadata+=("$line"); done < "$state"
  [[ ${#metadata[@]} -eq 5 && "${metadata[0]}" = "$destination" ]] || fail 'Invalid review metadata; cleanup refused.'
  [[ "$(git -C "$destination" rev-parse HEAD)" = "${metadata[1]}" ]] || fail 'Review HEAD changed; preserve the work before cleanup.'
  [[ -z "$(git -C "$destination" status --porcelain --untracked-files=all --ignored)" ]] || fail 'Worktree contains tracked, untracked or ignored work; cleanup refused.'
  # git worktree remove without --force also protects main checkouts/submodules.
  common=$(git -C "$destination" rev-parse --path-format=absolute --git-common-dir)
  git --git-dir="$common" worktree remove "$destination"
  echo 'Review worktree removed. Database migrations and server processes were not reverted.'
  ;;
*) usage; exit 1 ;;
esac
