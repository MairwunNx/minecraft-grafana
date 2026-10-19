# Minecraft dashboard for Grafana

<p align="center">
  <a href="https://grafana.com/grafana/dashboards/25941"><img alt="grafana.com" src="https://img.shields.io/badge/grafana.com-25941-F46800?logo=grafana&logoColor=white"></a>
  <a href="https://github.com/MairwunNx/minecraft-grafana/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/MairwunNx/minecraft-grafana?label=release"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/MairwunNx/minecraft-grafana"></a>
</p>

📈 A Grafana dashboard for a Minecraft server: how fast it ticks, what fills its worlds, who plays and what they do, and the chat. It draws the metrics of [minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter), which reads the server through [WorldAPI](https://github.com/MairwunNx/minecraft-worldapi).

[Русская версия](README.RU.md)

![The dashboard](media/dashboard.png)

## What's on it

- 🟢 **Server at a glance:** up or down, players online, TPS, tick time, heap, uptime, version.
- ⏱️ **Performance:** TPS, tick times by percentile against the 50 ms line where the server starts to lag, heap, CPU, garbage collection.
- 🌍 **Worlds:** loaded chunks, entities, block entities, the most common entities, weather, the day count.
- 🧑‍🤝‍🧑 **Players:** who's online with health, food, level, and ping, who played most in the time range, and every player's lifetime statistics: play time, last seen, advancements, deaths, mobs, blocks, diamonds, distance, experience.
- 💀 **Activity:** joins, deaths, and advancements over time, deaths by cause and killer, new players, and events from other plugins, like boss kills.
- 💬 **Chat and events** as tables, read straight from WorldAPI.

Pick a server and players at the top; restarts show as marks on every graph.

## Install

You need Grafana 11 or newer and Prometheus scraping [minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter#prometheus).

**From grafana.com.** In Grafana, open Dashboards → New → Import, enter `25941`, and pick your Prometheus.

**From a file.** Download [`minecraft.json`](https://github.com/MairwunNx/minecraft-grafana/releases/latest/download/minecraft.json) and import it the same way, or let Grafana load it from a provisioned folder: the dashboard picks its data sources through variables, so it needs no editing. minecraft-exporter's [`examples/`](https://github.com/MairwunNx/minecraft-exporter/tree/master/examples) shows a provisioned setup.

### Chat and event tables

These two tables ask WorldAPI directly, through the [Infinity](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/) data source:

1. Install Infinity: `grafana cli plugins install yesoreyeram-infinity-datasource`, or `GF_PLUGINS_PREINSTALL_SYNC=yesoreyeram-infinity-datasource` in Docker.
2. Add an Infinity data source. Set its URL to your WorldAPI, like `http://minecraft:8110/api/v1`, and its authentication to “Bearer token” with a WorldAPI token that has `events:read`, and `chat:read` for chat.
3. Pick it in the dashboard's “WorldAPI” variable.

WorldAPI records chat only with `events.chat: true` in its config. Grafana calls WorldAPI from its own server, so the token never reaches a browser. Anyone who can open the dashboard can read the chat, though: keep it off a public Grafana unless your players agree.

## Try it live

Moonlands, my hard survival server with friends, shows this dashboard to everyone: [minecraft.mairwunnx.com/grafana](https://minecraft.mairwunnx.com/grafana/d/minecraft-worldapi).

[![Play on Moonlands: pure vanilla, hard mobs, AI, claims. minecraft.mairwunnx.com](https://raw.githubusercontent.com/MairwunNx/minecraft-worldapi/master/media/og-adv-image.png)](https://minecraft.mairwunnx.com)

## License

[MIT](LICENSE).
