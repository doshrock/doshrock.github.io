# Google Reviews

The reviews section is self-hosted. There is no Elfsight widget any more.

## How it works

- `_data/google_reviews.json` holds every collected review (all ratings), plus the overall
  rating and review count.
- `assets/data/reviews.json` is built from it and keeps only the 5-star reviews.
- `_includes/reviews.html` fetches that file and shows 3 random 5-star reviews that have text.
  "Load More" adds 3 more.

## Daily update (cron on ubt)

```
0 6 * * * $HOME/doshrock-site/scripts/update_reviews.sh >> $HOME/.cache/doshrock-reviews/cron.log 2>&1
```

`update_reviews.sh` pulls `main`, runs `update_reviews.py`, and commits and pushes
`_data/google_reviews.json` only when something changed. GitHub Pages rebuilds on that push.

`update_reviews.py` calls the **legacy** Places API Place Details with `reviews_sort=newest`.
Places API (New) cannot sort reviews, and both return at most 5, so the job must run at least as
often as 5 new reviews can arrive. Daily is about 30 calls a month, inside the free 1,000.

- Google Cloud project: `doshrock-web` (billing account "Doshrock")
- Key: `GOOGLE_PLACES_API_KEY` in `~/.config/doshrock-reviews/env` on ubt, restricted to
  Places API and Places API (New)
- Place ID: `ChIJdzpxhZA7yUwRql6GdYlUaIw`
- Exit code 3 means "no new reviews" and is not an error.

Run by hand:

```bash
set -a; . ~/.config/doshrock-reviews/env; set +a
python3 scripts/update_reviews.py
```

## History

The first 287 reviews were collected from the Google Maps page on 2026-10-01. Those entries
have `"approx": true` because Maps only shows relative dates ("2 years ago"). The API replaces
the time with the exact one when it sees the same review again.
