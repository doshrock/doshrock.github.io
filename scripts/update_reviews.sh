#!/usr/bin/env bash
# Daily cron on ubt: pull, merge the newest Google reviews, push only if something changed.
set -euo pipefail

REPO="${REPO:-$HOME/doshrock-site}"
ENV_FILE="${ENV_FILE:-$HOME/.config/doshrock-reviews/env}"

set -a
# shellcheck source=/dev/null
source "$ENV_FILE"
set +a

cd "$REPO"
git pull -q --ff-only origin main

rc=0
python3 scripts/update_reviews.py || rc=$?
if [ "$rc" -eq 3 ]; then
    exit 0
elif [ "$rc" -ne 0 ]; then
    exit "$rc"
fi

git add _data/google_reviews.json
git commit -q -m "Pull in the latest Google reviews"
git push -q origin main
