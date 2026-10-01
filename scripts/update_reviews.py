#!/usr/bin/env python3
"""Merge the newest Google reviews into _data/google_reviews.json.

Uses the legacy Places API because it is the only one that sorts reviews by
newest; it returns at most 5 per call, so this has to run at least as often
as 5 new reviews can arrive (daily is plenty).

Exit codes: 0 = file changed, 3 = nothing new, anything else = error.
"""
from __future__ import annotations

import datetime
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "_data" / "google_reviews.json"
DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
NO_CHANGE = 3


def fetch(place_id: str, key: str) -> dict:
    query = urllib.parse.urlencode({
        "place_id": place_id,
        "fields": "rating,user_ratings_total,reviews",
        "reviews_sort": "newest",
        "reviews_no_translations": "true",
        "key": key,
    })
    with urllib.request.urlopen(f"{DETAILS_URL}?{query}", timeout=30) as resp:
        body = json.load(resp)
    if body.get("status") != "OK":
        raise RuntimeError(f"Places API {body.get('status')}: {body.get('error_message', '')}")
    return body["result"]


def same_review(stored: dict, fresh: dict) -> bool:
    if stored["name"] != fresh["author_name"]:
        return False
    if stored.get("approx"):
        # Scraped entries only have a relative date, so match on the text instead.
        return stored["text"].strip() == fresh.get("text", "").strip()
    return stored["time"] == fresh["time"]


def merge(data: dict, result: dict) -> bool:
    changed = False
    for field, src in (("rating", "rating"), ("total", "user_ratings_total")):
        if src in result and data.get(field) != result[src]:
            data[field] = result[src]
            changed = True

    for fresh in result.get("reviews", []):
        match = next((r for r in data["reviews"] if same_review(r, fresh)), None)
        if match is None:
            data["reviews"].insert(0, {
                "name": fresh["author_name"],
                "avatar": fresh.get("profile_photo_url", ""),
                "rating": fresh["rating"],
                "time": fresh["time"],
                "approx": False,
                "text": fresh.get("text", "").strip(),
            })
            changed = True
        elif match.get("approx"):
            # The API gives the exact timestamp the scrape could not.
            match["time"] = fresh["time"]
            match["approx"] = False
            changed = True

    if changed:
        data["reviews"].sort(key=lambda r: r["time"], reverse=True)
        data["updated"] = datetime.date.today().isoformat()
    return changed


def main() -> int:
    key = os.environ.get("GOOGLE_PLACES_API_KEY")
    if not key:
        print("GOOGLE_PLACES_API_KEY is not set", file=sys.stderr)
        return 1

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    before = len(data["reviews"])
    if not merge(data, fetch(data["place_id"], key)):
        print("no new reviews")
        return NO_CHANGE

    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"reviews {before} -> {len(data['reviews'])}, rating {data['rating']}, total {data['total']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
