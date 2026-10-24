"""Checks dashboard.json for what breaks imports or provisioning. Run: python3 -I scripts/check.py"""

import json
import re
import sys
from pathlib import Path

DASHBOARD = Path(__file__).resolve().parent.parent / "dashboard.json"
DATASOURCES = {"prometheus": "${datasource}", "yesoreyeram-infinity-datasource": "${worldapi}"}

problems = []
dashboard = json.loads(DASHBOARD.read_text(encoding="utf-8"))
text = DASHBOARD.read_text(encoding="utf-8")


def walk(panels):
    for panel in panels:
        yield panel
        yield from walk(panel.get("panels", []))


if dashboard.get("uid") != "minecraft-worldapi":
    problems.append("the uid must stay minecraft-worldapi: links and Moonlands point at it")
if "${DS_" in text:
    problems.append("an ${DS_…} input: provisioned files can't fill it; use the datasource variables")

ids = set()
for panel in walk(dashboard["panels"]):
    title = panel.get("title", "?")
    if panel["id"] in ids:
        problems.append(f"{title}: id {panel['id']} repeats")
    ids.add(panel["id"])
    grid = panel["gridPos"]
    if grid["x"] + grid["w"] > 24:
        problems.append(f"{title}: wider than the grid")
    if panel["type"] == "row":
        continue
    for target in [panel] + panel.get("targets", []):
        source = target.get("datasource")
        if source and DATASOURCES.get(source.get("type")) != source.get("uid"):
            problems.append(f"{title}: data source {source} isn't one of the variables")
    for target in panel.get("targets", []):
        # Infinity sends WorldAPI's token along: a query may only read.
        method = target.get("url_options", {}).get("method", "GET")
        if "url" in target and method != "GET":
            problems.append(f"{title}: Infinity query uses {method}; only GET may reach WorldAPI")
        for metric in re.findall(r"\b([a-z_]+)\{", target.get("expr", "")):
            if not metric.startswith("minecraft_"):
                problems.append(f"{title}: {metric} isn't a minecraft-exporter metric")

for problem in problems:
    print(f"::error::{problem}")
if problems:
    sys.exit(1)
print(f"dashboard.json: {len(ids)} panels look right")
