"""Checks dashboard.json for what breaks imports or provisioning. Run: python3 -I scripts/check.py"""

import json
import re
import sys
from pathlib import Path

DASHBOARD = Path(__file__).resolve().parent.parent / "dashboard.json"
DATASOURCES = {"prometheus": "${datasource}", "yesoreyeram-infinity-datasource": "${worldapi}"}
# Built in to Grafana, not a data source someone picks.
BUILT_IN = {"grafana", "datasource"}

problems = []
dashboard = json.loads(DASHBOARD.read_text(encoding="utf-8"))
text = DASHBOARD.read_text(encoding="utf-8")
spec = dashboard.get("spec", {})


def check_query(title, query):
    group, source = query.get("group"), query.get("datasource", {}).get("name")
    if group not in BUILT_IN and DATASOURCES.get(group) != source:
        problems.append(f"{title}: data source {group} {source} isn't one of the variables")
    body = query.get("spec", {})
    # Infinity sends WorldAPI's token along: a query may only read.
    method = body.get("url_options", {}).get("method", "GET")
    if "url" in body and method != "GET":
        problems.append(f"{title}: Infinity query uses {method}; only GET may reach WorldAPI")
    for metric in re.findall(r"\b([a-z_]+)\{", body.get("expr", "") + body.get("query", "")):
        if not metric.startswith("minecraft_"):
            problems.append(f"{title}: {metric} isn't a minecraft-exporter metric")


# Grafana 13 hides rows by a condition only in the v2 schema, so the file stays a v2 resource.
if not dashboard.get("apiVersion", "").startswith("dashboard.grafana.app/v2") or dashboard.get("kind") != "Dashboard":
    sys.exit("::error::dashboard.json must be a v2 dashboard: rows hide by conditions only there")
if dashboard.get("metadata", {}).get("name") != "minecraft-worldapi":
    problems.append("the uid (metadata.name) must stay minecraft-worldapi: links and Moonlands point at it")
if set(dashboard.get("metadata", {})) != {"name"}:
    problems.append("metadata holds only name: an export's namespace, uid, and resourceVersion belong to one Grafana")
if spec.get("title") != "Minecraft server (minecraft-exporter)":
    problems.append("the title must stay “Minecraft server (minecraft-exporter)”, as on grafana.com")
if "${DS_" in text:
    problems.append("an ${DS_…} input: provisioned files can't fill it; use the datasource variables")

ids = set()
elements = spec.get("elements", {})
for key, element in elements.items():
    panel = element["spec"]
    title = panel.get("title", key)
    if panel["id"] in ids:
        problems.append(f"{title}: id {panel['id']} repeats")
    ids.add(panel["id"])
    for query in panel["data"]["spec"]["queries"]:
        check_query(title, query["spec"]["query"])

placed = set()
variables = {variable["spec"]["name"] for variable in spec.get("variables", [])}
for row in spec["layout"]["spec"]["rows"]:
    row = row["spec"]
    if "repeat" in row:
        problems.append(f"{row['title']}: a row repeated over an empty variable still shows; use a condition")
    for condition in row.get("conditionalRendering", {}).get("spec", {}).get("items", []):
        if condition["kind"] == "ConditionalRenderingVariable" and condition["spec"]["variable"] not in variables:
            problems.append(f"{row['title']}: its condition reads a variable that doesn't exist")
    for item in row["layout"]["spec"]["items"]:
        item = item["spec"]
        name = item["element"]["name"]
        placed.add(name)
        if name not in elements:
            problems.append(f"{row['title']}: places {name}, which doesn't exist")
        elif item["x"] + item["width"] > 24:
            problems.append(f"{elements[name]['spec']['title']}: wider than the grid")
for name in elements.keys() - placed:
    problems.append(f"{elements[name]['spec']['title']}: no row places it")

for variable in spec.get("variables", []):
    if "query" in variable["spec"]:
        check_query(f"variable {variable['spec']['name']}", variable["spec"]["query"])
for annotation in spec.get("annotations", []):
    query = annotation["spec"]["query"]
    check_query(f"annotation {annotation['spec']['name']}", query)
    expr = annotation["spec"].get("legacyOptions", {}).get("expr", "")
    check_query(f"annotation {annotation['spec']['name']}", {"group": "grafana", "spec": {"expr": expr}})

for problem in problems:
    print(f"::error::{problem}")
if problems:
    sys.exit(1)
print(f"dashboard.json: {len(ids)} panels look right")
