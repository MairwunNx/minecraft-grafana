# minecraft-grafana: notes for AI agents

A Grafana dashboard for the metrics of minecraft-exporter (MairwunNx/minecraft-exporter, `~/c/personal/minecraft-exporter`), with chat and event tables read from WorldAPI through the Infinity data source. README.md explains it for humans; read it first. Moonlands, the owner's server, provisions it in `~/c/personal/minecraft` (MairwunNx/minecraft) as `monitoring/grafana/dashboards/minecraft-worldapi.json`.

## Talking to the owner

- Reply in Russian, address the owner as «вы». Quotes «ёлочки», nested „лапки“, an em dash with spaces « — ».
- Panel titles, descriptions, commit messages, and README.md are in English: curly quotes, an em dash without spaces or an en dash with spaces, never a hyphen as a dash. README.RU.md follows the Russian rules.

## How it fits together

| Path | What it does |
|---|---|
| `dashboard.json` | The dashboard, the only source: edit it, never a copy |
| `scripts/check.py` | What CI checks: the uid, unique ids, the grid, data sources through variables, `minecraft_` metrics only |
| `media/dashboard.png` | The screenshot in both READMEs and on grafana.com |

## Rules that keep it working

- The uid stays `minecraft-worldapi`: Moonlands' links and both READMEs point at `/d/minecraft-worldapi/minecraft`.
- Data sources come only from the `datasource` (Prometheus) and `worldapi` (Infinity) variables. `${DS_…}` inputs work on import but not in a provisioned file, which Moonlands uses.
- Every query filters by `instance="$instance"`, and per-player ones by `player=~"$player"` too.
- Use only metrics minecraft-exporter documents in its README. A new metric lands in the exporter first, and the dashboard's release follows the exporter's.
- Counters that start with the exporter (events, deaths by cause) lose their first event under `increase()`; the exporter seeds what it can at zero, and “Deaths by cause” subtracts the value at the start of the range instead.
- Follow the dataviz rules the panels already use: stats for headline numbers, one axis per graph, status colors only for thresholds, thin lines.

## Checking a change

1. `python3 -I scripts/check.py`.
2. Run minecraft-exporter's `examples/` stack with `WORLDAPI_URL=https://minecraft.mairwunnx.com/worldapi/api/v1` (read-only; `WORLDAPI_TOKEN` from `~/.secrets/cloud.env` fills the chat table) and copy `dashboard.json` to `examples/grafana/dashboards/minecraft.json`; Grafana reloads it within seconds. Look at it in a browser at `http://localhost:3000`: every panel shows data, nothing overlaps, the tables have all their columns. Fresh Prometheus data needs half an hour before the bar charts fill.
3. When a panel was edited in Grafana's editor, save it there, then Export → Export as JSON with “Export for sharing externally” off, and replace `dashboard.json` with it.

## Docs and releases

- README.md and README.RU.md: what's on the dashboard and how to import it. Change both together; refresh `media/dashboard.png` when the look changes (1600 px wide, Moonlands' data, the last 24 hours).
- After a change, add it to CHANGELOG.md in the same push: under the topmost “## X.Y.Z” section while that version isn't released (`gh release view vX.Y.Z` fails), or under a new section with the next version.
- Release: `gh workflow run release.yml -R MairwunNx/minecraft-grafana -f version=X.Y.Z`. It attaches `minecraft.json`, the dashboard with the version in its description, to the GitHub release; `releases/latest/download/minecraft.json` always reaches the newest. Its `deploy` job starts `ship-plugin.yml` in MairwunNx/minecraft, which copies it over Moonlands' file.
- grafana.com has no API for new revisions, so upload each release on the website: sign in as the owner, open the dashboard GRAFANA_ID under “My dashboards”, Revisions → upload `minecraft.json` from the release, and update the README and screenshot there when they changed. The owner signs in; ask when you can't reach the account.

## Commits

Short one-line imperative English messages, one logical change per commit: “Show deaths by killer”.
