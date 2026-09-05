# Juan Martinez — Portfolio

Public portfolio at https://josejuanmartinez.github.io/.

Static HTML, CSS and JavaScript. Game previews are optimized, muted MP4 loops with downloadable GIF versions. Source recordings stay local.

## Update

Edit `repos.json` (public repositories only), then run `python build.py` to refresh the page. Edit `style.css` and `app.js` directly. Media lives in `assets/`.

GitHub Pages serves the root directory of the `main` branch. Push changes to publish.

## Project diagrams

`project-notes.json` records summaries, source links, and individual visual explanations based on each repository's README (and root files for sparse documentation). These diagrams describe concepts and workflows, not benchmark results.

Run `python render_diagrams.py` to create the 240 x 120 pixel PNG figures in `assets/figures/`, then `python build.py` to update the page. Diagram rendering uses Pillow. The site serves only compact diagrams and real gameplay media; earlier decorative illustrations are no longer referenced.

Each project has a bespoke composition: matrices for LoRA, route grids for pathfinding, token spans for NLP, interaction loops for RL, and domain-specific views for other projects. Any sample points or attributions are conceptual examples, not measured results.
