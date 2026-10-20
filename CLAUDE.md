# minecraft-grafana: notes for AI agents

A Grafana dashboard for the metrics of minecraft-exporter (MairwunNx/minecraft-exporter, `~/c/personal/minecraft-exporter`), with chat and event tables read from WorldAPI through the Infinity data source. README.md shows it off; the [wiki](https://github.com/MairwunNx/minecraft-grafana/wiki) is the manual (installation, data sources, every panel, editing, releasing); read both first. Moonlands, the owner's server, provisions it in `~/c/personal/minecraft` (MairwunNx/minecraft) as `monitoring/grafana/dashboards/minecraft-worldapi.json`.

## Talking to the owner

- Reply in Russian, address the owner as «вы». Quotes «ёлочки», nested „лапки“, an em dash with spaces « — ».
- Panel titles, descriptions, commit messages, and README.md are in English: curly quotes, an em dash without spaces or an en dash with spaces, never a hyphen as a dash. README.RU.md follows the Russian rules.

## How it fits together

| Path | What it does |
|---|---|
| `dashboard.json` | The dashboard, the only source: edit it, never a copy |
| `scripts/check.py` | What CI checks: the uid, unique ids, the grid, data sources through variables, `minecraft_` metrics only |
| `media/*.png` | The screenshots in both READMEs and on grafana.com, one per group of rows |

## Rules that keep it working

- The uid stays `minecraft-worldapi`: Moonlands' links, both READMEs, and grafana.com point at `/d/minecraft-worldapi`. The title stays “Minecraft server (minecraft-exporter)”, as on grafana.com: imports match it, and Grafana refuses two dashboards with one title in a folder.
- Data sources come only from the `datasource` (Prometheus) and `worldapi` (Infinity) variables. `${DS_…}` inputs work on import but not in a provisioned file, which Moonlands uses.
- Every query filters by `instance="$instance"`, and per-player ones by `player=~"$player"` too.
- Use only metrics minecraft-exporter documents on its wiki's Metrics page. A new metric lands in the exporter first, and the dashboard's release follows the exporter's.
- Counters that start with the exporter (events, deaths by cause) lose their first event under `increase()`; the exporter seeds what it can at zero, and “Deaths by cause” subtracts the value at the start of the range instead.
- Panels that need a WorldAPI permission say so in their description, as “Needs a WorldAPI token with logs:read.”, and the README's warning about keeping a token-fed dashboard private stays.
- Follow the dataviz rules the panels already use: stats for headline numbers, one axis per graph, status colors only for thresholds, thin lines.

## Checking a change

1. `python3 -I scripts/check.py`.
2. Run minecraft-exporter's `examples/` stack with `WORLDAPI_URL=https://minecraft.mairwunnx.com/worldapi/api/v1` (read-only; `WORLDAPI_TOKEN` from `~/.secrets/cloud.env` fills the chat table) and copy `dashboard.json` to `examples/grafana/dashboards/minecraft.json`; Grafana reloads it within seconds. Look at it in a browser at `http://localhost:3000`: every panel shows data, nothing overlaps, the tables have all their columns. Fresh Prometheus data needs half an hour before the bar charts fill.
3. When a panel was edited in Grafana's editor, save it there, then Export → Export as JSON with “Export for sharing externally” off, and replace `dashboard.json` with it.

## Docs and releases

- README.md and README.RU.md only show the dashboard off: what you get, a 3-step Get started, links into the wiki, Related projects. Change both together; refresh the screenshots in `media/` when the look changes (1600 px wide, the last 24 hours, one per group of rows). They show made-up data, so every panel draws something: minecraft-exporter's `examples/mock/` fakes a day of a busy server.
- The manual lives in the GitHub wiki (`https://github.com/MairwunNx/minecraft-grafana.wiki.git`, English only). When a panel, variable, or permission changes, update “What the dashboard shows”, “Data sources”, or “Variables” there; release steps live in “Releasing”.
- After a change, add it to CHANGELOG.md in the same push: under the topmost “## X.Y.Z” section while that version isn't released (`gh release view vX.Y.Z` fails), or under a new section with the next version.
- Release: `gh workflow run release.yml -R MairwunNx/minecraft-grafana -f version=X.Y.Z`. It attaches `minecraft.json`, the dashboard with the version in its description, to the GitHub release; `releases/latest/download/minecraft.json` always reaches the newest. Its `deploy` job starts `ship-plugin.yml` in MairwunNx/minecraft, which copies it over Moonlands' file.
- grafana.com has no API for new revisions, so upload each release on the website: the dashboard is [25941](https://grafana.com/grafana/dashboards/25941) in the owner's organization `mairwunnx` (`https://grafana.com/orgs/mairwunnx/dashboards`). Signed in, open its public page, [grafana.com/grafana/dashboards/25941](https://grafana.com/grafana/dashboards/25941/), switch to the Revisions tab, and upload `minecraft.json` from the release with “Upload revision”. The README and screenshot there change in the form at `https://grafana.com/orgs/mairwunnx/dashboards/25941/edit`; keep its README a shorter take on README.md, warning included. The owner signs in; ask when you can't reach the account.
- That site's forms ignore values set by script: click into a field, type, and press Tab before Save, then check what stuck with `GET https://grafana.com/api/dashboards/25941`. Its README there is a shorter take on README.md.

## Commits

Short one-line imperative English messages, one logical change per commit: “Show deaths by killer”.
