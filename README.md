# Mike Xiangyu Liu — research website

Personal research website built with [al-folio v1.2](https://github.com/alshedivat/al-folio/releases/tag/v1.2), Jekyll 4, and the pinned `al_folio_core` theme gem. The theme runtime stays in Ruby gems; this repository contains personal content and a small styling layer.

## Local development

Use Ruby 3.3.10 (see `.ruby-version`) and Bundler:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve --config _config.yml,_config.dev.yml
```

Open <http://127.0.0.1:4000>. Node.js and ImageMagick are not needed. The previous template's tracked `node_modules` directory is excluded from the site and unused.

To build and verify the production output:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
bundle exec al-folio upgrade audit
bundle exec al-folio upgrade overrides audit
```

## Content

- `_pages/about.md`: minimal homepage with profile links and project cards.
- `_projects/*.md`: project descriptions, ordering, authors, and resource links. All three existing `/projects/…/` URLs are preserved.
- `_bibliography/papers.bib`: publication records, rendered by Jekyll Scholar.
- `_pages/cv.md`: link to the existing current CV on Google Drive. Set `cv_url` in `_config.yml` to update it.
- `_data/socials.yml` and `_config.yml`: profile and site metadata.
- `_includes/research_cards.liquid`: shared project cards.
- `_layouts/research.liquid`: project detail pages.
- `_sass/_personal.scss`: personal layout and responsive styles.
- `assets/css/main.scss`: al-folio Sass entry point with a teal palette and the personal stylesheet. Its upstream version is recorded in `.al-folio-overrides.yml`.

Project PDFs, videos, images, and previously uploaded files retain their original locations. CoDE-SLAM remains marked as coming soon. The old theme's fictional publications, CV entries, blog posts, teaching entries, and sample pages have been removed.

## GitHub Pages

The workflow in `.github/workflows/deploy.yml` builds and validates pull requests. Pushes to `master` or `main` build and deploy using the official GitHub Pages artifact workflow.

**One-time repository setting:** under **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. The old built-in GitHub Pages Jekyll build cannot load al-folio's custom gems. No deployment occurs merely from editing this checkout or pushing a feature branch.

## Updating al-folio

Update the pinned al-folio gem versions in `Gemfile`, run `bundle update`, and review `bundle exec al-folio upgrade audit`. When the upstream CSS entry point changes, compare it with the local override before acknowledging it:

```sh
bundle exec al-folio upgrade overrides diff assets/css/main.scss
bundle exec al-folio upgrade overrides accept assets/css/main.scss
```

Commit the resulting `Gemfile.lock` and `.al-folio-overrides.yml`. Both the original theme's and al-folio's MIT notices are retained in `LICENSE`.
