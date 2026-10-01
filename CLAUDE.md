# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based static website for Doshrock, a Korean restaurant in Montreal, Canada. The site is hosted on GitHub Pages at doshrock.com and supports three languages: French (default), English, and Korean.

## Technology Stack

- Jekyll 3.9.0 (static site generator)
- Bootstrap 3.x for styling
- jQuery, WOW.js, Animate.css for animations
- SASS/SCSS for stylesheets
- Liquid templating engine
- GitHub Pages deployment with GitHub Actions

## Development Commands

**Start development server:**
```bash
bundle exec jekyll serve
# Site available at http://localhost:4000
```

**Build site:**
```bash
bundle exec jekyll build
```

**Install dependencies:**
```bash
bundle install
```

**Note:** Changes to `_config.yml` require a server restart. Layout and include changes are hot-reloaded.

## High-Level Architecture

### Multi-language System

The site uses a custom internationalization system with three components:

1. **Translation tokens**: Stored in `_data/i18n/{en,fr,kr}.yml`
2. **i18n include**: `_includes/i18n.html` resolves tokens to translations
3. **Language-specific pages**: Entry points like `index.markdown`, `index-en.markdown`, etc.

Usage in templates:
```liquid
{%- include i18n.html token='section_name' -%}
```

Always update all three language files when adding new translatable content.

### Menu Data System

Menus are data-driven from YAML files in `_data/menu/`:
- `01.appetizer.yml` - Appetizers/Bunsik
- `02.doshrock_dupbap.yml` - Dupbap dishes
- `03.bibimbap_jjigae.yml` - Bibimbap & stews
- `04.anju_dessert.yml` - Side dishes & desserts

**Menu item structure:**
```yaml
- id: unique_id
  name: "한글 이름"
  name_en: "English Name"
  name_fr: "Nom français"
  name_kr: "한글 이름"
  tag_en: ["tag1", "tag2"]
  tag_fr: ["étiquette1", "étiquette2"]
  tag_kr: ["태그1", "태그2"]
  image: "menu/path/to/image.jpg"
  prices:
    - quantity: "1 portion"
      price: 12.99
```

All four name fields are required. Tags are used for filtering in the full menu views.

### Layout System

Key layouts in `_layouts/`:
- `front.html` - Main homepage with scrolling sections
- `full_menu.html` - Full menu with JavaScript-based tag filtering
- `menu_layout.html` - Base menu layout (parent of full_menu variants)
- `online_order.html` - Embeds order-online.ai iframe
- `table_order.html` - Grid of 20 table links to ClusterPOS

### Third-Party Integrations

- **ClusterPOS**: Table ordering system with 20 unique table UUIDs configured in `_config.yml` under `table_order`
- **order-online.ai**: Online ordering iframe at doshrock.order-online.ai
- **Google Analytics**: Tracking ID G-7Z8LPXHRQF
- **Google Maps**: Embedded in contact section
- **Google Reviews**: Self-hosted, no widget. See `UPDATE_REVIEWS.md`.

## Key Development Patterns

### Changing Menu Prices

Prices on `/full_menu*` come from `assets/data/menu.xml`, a copy of the ClusterPOS menu XML
with multilingual descriptions added by `update_xml.py`. Change only the `Price` attribute of
the `<Item tUID="...">` you need; the tUID matches the POS item id. Do not replace the whole
file with a fresh POS export or the descriptions are lost.

The printed menu scans are `img/menu/print/menu2026_1..4.jpg` (1280x1810, exported from the
menu PSDs).

### Adding Translations

1. Add key-value pairs to all three files: `_data/i18n/en.yml`, `fr.yml`, `kr.yml`
2. Use the i18n include in templates: `{%- include i18n.html token='your_key' -%}`
3. The include automatically uses the language from `page.lang` or `site.lang`

### Contact Information

Restaurant details are configured in `_config.yml`:
- Phone: +1 579-423-5742
- Email: doshrock.com@gmail.com
- Instagram: doshrock.mtl
- Facebook: doshrock.mtl

Operating hours are hardcoded in `_includes/contact.html` (not in config).

## Site Structure

```
_layouts/          → Page templates
_includes/         → Reusable HTML components (header, nav, menu, contact, etc.)
_data/
  ├── i18n/       → Translation files (en.yml, fr.yml, kr.yml)
  └── google_reviews.json → All collected Google reviews (updated daily by cron)
assets/data/      → menu.xml (menu + prices), reviews.json (built from google_reviews.json)
scripts/          → update_reviews.py / .sh (excluded from the site build)
_sass/            → SASS partials
css/              → Compiled stylesheets
js/               → JavaScript (jQuery, Bootstrap, custom)
img/menu/         → Menu item images
```

## Deployment

The site automatically deploys via GitHub Actions (`.github/workflows/jekyll.yml`) when pushing to the `main` branch. The workflow uses a Docker-based Jekyll builder and publishes to GitHub Pages at doshrock.com.

## Important Notes

- This site uses Bootstrap 3.x (not Bootstrap 4 or 5)
- jQuery is required for Bootstrap components and WOW.js animations
- SASS is compiled by Jekyll (no separate build tool needed)
- All menu images should be placed in `img/menu/` with appropriate subdirectories
- The site is responsive and mobile-friendly using Bootstrap's grid system
