# Minecraft dashboard for Grafana

<p align="center">
  <a href="https://grafana.com/grafana/dashboards/25941"><img alt="grafana.com" src="https://img.shields.io/badge/grafana.com-25941-F46800?logo=grafana&logoColor=white"></a>
  <a href="https://github.com/MairwunNx/minecraft-grafana/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/MairwunNx/minecraft-grafana?label=release"></a>
  <img alt="Grafana 13+" src="https://img.shields.io/badge/Grafana-13%2B-F46800?logo=grafana&logoColor=white">
  <a href="https://github.com/MairwunNx/minecraft-grafana/actions/workflows/ci.yml"><img alt="Check" src="https://img.shields.io/github/actions/workflow/status/MairwunNx/minecraft-grafana/ci.yml?branch=master&label=check"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/MairwunNx/minecraft-grafana"></a>
</p>

📈 A Grafana dashboard for a Minecraft server on Paper, Fabric, or NeoForge, or for the world you play alone: how fast it ticks, what fills its worlds, who plays and what they do, and the chat. It draws the metrics of [minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter), which reads the server through [WorldAPI](https://github.com/MairwunNx/minecraft-worldapi).

[Русская версия](README.RU.md)

![Server, performance, and host](media/overview.png)

## What you get

- 🟢 **Server at a glance:** up, down, or paused, version, uptime, TPS, tick time, heap.
- ⏱️ **Performance:** TPS, tick times by percentile against the 50 ms line where the server starts to lag, heap, CPU, garbage collection.
- 🌍 **Worlds:** loaded chunks, entities, block entities, the most common entities, a weather timeline, the day and the time of day.
- 👥 **Players:** who’s online, where they stand, their health, food, level, ping, and time played; who played most in the time range; every player’s lifetime statistics, from deaths to diamonds.
- 💀 **Activity:** joins, deaths, and advancements over time, deaths by cause and killer, chat by player, new players, and other plugins’ events.
- 💬 **Chat, events, and console warnings** as tables, read straight from WorldAPI.
- 🔐 **More with a WorldAPI token:** the host’s load and disk, what lags in each world down to the busiest chunks, plugins with their versions, and the console.
- 🎮 **Your world, alone:** for a singleplayer world it hides the server’s players, console, and chat, and shows your play time, level, deaths, diamonds, health and food, and mods.
- 🛰️ **Many servers, one dashboard:** pick a server and players at the top; restarts show as marks on every graph.

### A look around

Worlds and what crowds them, down to the busiest chunks:

![Worlds and lag sources](media/worlds.png)

Who’s online, where, and how they’re doing, and every player’s lifetime statistics:

![Players](media/players.png)

What players did in the time range:

![Activity](media/activity.png)

Plugins, the console, the chat, and events:

![Plugins, console, chat, and events](media/console.png)

The screenshots show a made-up server, so every panel has something to draw.

> [!WARNING]
> **Keep this dashboard private when a token feeds it.** Every viewer of a Grafana can send any query to its data sources and read everything the token may: chat, the console, every player’s position. [Keeping it private](https://github.com/MairwunNx/minecraft-grafana/wiki/Keeping-it-private) says what to do.

## Get started

1. In Grafana 13 or newer, open **Dashboards → New → Import** and enter `25941`, or upload [`minecraft.json`](https://github.com/MairwunNx/minecraft-grafana/releases/latest/download/minecraft.json) from the latest release.
2. Pick the Prometheus that scrapes [minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter), and, for the chat and event tables, an [Infinity data source](https://github.com/MairwunNx/minecraft-grafana/wiki/Data-sources) pointed at WorldAPI.
3. Done: open the dashboard and pick your server at the top.

## Documentation

The [wiki](https://github.com/MairwunNx/minecraft-grafana/wiki) has everything, step by step.

**For server owners:** [Installation](https://github.com/MairwunNx/minecraft-grafana/wiki/Installation) · [Data sources](https://github.com/MairwunNx/minecraft-grafana/wiki/Data-sources) · [Keeping it private](https://github.com/MairwunNx/minecraft-grafana/wiki/Keeping-it-private) · [What the dashboard shows](https://github.com/MairwunNx/minecraft-grafana/wiki/What-the-dashboard-shows) · [Variables](https://github.com/MairwunNx/minecraft-grafana/wiki/Variables) · [Troubleshooting](https://github.com/MairwunNx/minecraft-grafana/wiki/Troubleshooting)

**For developers:** [Editing the dashboard](https://github.com/MairwunNx/minecraft-grafana/wiki/Editing-the-dashboard) · [Releasing](https://github.com/MairwunNx/minecraft-grafana/wiki/Releasing)

## Related projects

- **[Moonlands](https://minecraft.mairwunnx.com)** – the hard-survival server where all of these run.
- **[WorldAPI](https://github.com/MairwunNx/minecraft-worldapi)** – REST and WebSocket API to the world, players, and stats of a Paper, Fabric, or NeoForge server.
- **[Minecraft MCP](https://github.com/MairwunNx/minecraft-mcp)** – lets an AI client read and run a server through WorldAPI.
- **[Allay](https://github.com/allay-ai/minecraft)** – an AI helper in the game: ask with `/ask`, right in the chat.
- **[Allay Server](https://github.com/allay-ai/server)** – the backend behind Allay.
- **[Mo’Joins](https://github.com/MairwunNx/mojoins)** – join and quit messages in each player’s language.
- **[Mo’Afks](https://github.com/MairwunNx/moafks)** – a safe AFK mode that doesn’t block the night.
- **[Mo’Bosses](https://github.com/MairwunNx/mobosses)** – monsters that spawn as bosses with classes, abilities, and loot.
- **[minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter)** – Prometheus metrics from WorldAPI.

Moonlands, my hard survival server with friends, runs this dashboard in a private Grafana. Its site shows the players and the hall of fame to everyone.

[![Play on Moonlands: pure vanilla, hard mobs, AI, claims. minecraft.mairwunnx.com](https://raw.githubusercontent.com/MairwunNx/minecraft-worldapi/master/media/og-adv-image.png)](https://minecraft.mairwunnx.com)

> 🫡 Made by Pavel Erokhin (Павел Ерохин), aka mairwunnx.
