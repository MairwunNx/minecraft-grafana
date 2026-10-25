# Changelog

## 1.5.0

For minecraft-exporter 3.1.0 or newer, which labels where WorldAPI runs. With an older exporter every server reads as a dedicated one and the dashboard looks as before.

- 🎮 **A row for singleplayer.** For a singleplayer world (`side="integrated"`), “Your world” shows whether the game runs or sits paused, play time, level, deaths, diamonds, advancements, health and food, and the mods.
- 🙈 **No server rows alone.** Players, “Plugins and console”, and “Chat and events” show for servers only, through the hidden `multiplayer` and `singleplayer` variables.
- ⏸️ **Status knows “Paused”**, and the TPS tile's description says a paused game doesn't tick.
- 🧩 **Plugins and mods.** The table is “Plugins and mods”, with a `Kind` column from minecraft-exporter's new label, for Fabric and NeoForge servers.
- 🔢 **The player counts moved.** “Players online” and “Players ever” open the Players row; the top row keeps six tiles.
- The Version tile leaves out an empty build, as on Fabric and NeoForge: “Fabric 26.3”.

## 1.4.1

- 🐛 The “Day” tile shows the whole number, such as 1094, instead of “1K”.

## 1.4.0

For minecraft-exporter 3.0.0 or newer.

- 💥 **The day comes from `minecraft_world_days`,** the gauge minecraft-exporter 3.0.0 exports in place of `minecraft_world_days_total`. With an older exporter, the “Day” tile stays empty.
- **Removed: the Mo’Bosses row.** It read one plugin's data, which doesn't belong in a dashboard for any server.
- The READMEs and grafana.com show fresh screenshots of the current rows.

## 1.3.0

For minecraft-exporter 2.0.0 or newer; checked against WorldAPI 4.0.0.

- ⚔️ **Mo’Bosses is back, read from WorldAPI.** A folded row shows bosses alive, spawned, and killed, every boss type and class, and the 50 best hunters, through the Infinity data source at `/extensions/mobosses`. It needs Mo’Bosses, 2.9.0 or newer with WorldAPI 4.0; on a server without it, the row shows errors and the rest of the dashboard stays as it was.
- **Failed requests** count in five-minute bars that don't overlap, so a bar shows how many requests failed in its five minutes.
- The check in CI refuses an Infinity query that isn't a `GET`: Infinity sends WorldAPI's token along, and a dashboard only reads.

## 1.2.0

For minecraft-exporter 2.0.0; it works with 1.1.0 too.

- **Server:** the tiles go from the server to the players to performance: status, version, uptime, players online and ever, TPS, tick time, heap.
- **Worlds:** the weather timeline names its states in a legend, a rain with thunder counts as a thunderstorm, and the day, the time of day, and the weather now sit in tiles of their own.
- **Players:** “Online now” adds idle time, time played in the range and in all, deaths, and advancements, with bars for health and food. “Every player” adds players killed, hearts lost, items crafted, and trades.
- **Rankings as tables:** the most common entities, time played, deaths by cause, chat by player, and warnings by source show full names with a bar each, and a source shows its short name.
- **Plugins:** the plugin list moves next to the console; the bans, operators, whitelist, and Mo’Bosses panels are gone.
- The READMEs show one screenshot per group of rows, taken on a made-up server.

## 1.1.0

For minecraft-exporter 1.1.0 and a WorldAPI token behind it.

- **Host:** load against the CPU count, memory, free disk, and open files.
- **Lag sources:** items on the ground, villagers, pets and named mobs, and a table of the busiest chunks with their entities, block entities, and hoppers.
- **Plugins:** the plugin list with versions, bans, operators, the whitelist, and Mo’Bosses' bosses alive, spawned, and killed by class.
- **Console:** lines by level, warnings and errors by source, and a table of the latest warnings and errors read from WorldAPI.
- **Players:** coordinates in “Online now”, and chat messages by player.
- **Exporter:** a table of the endpoints the token opens; failed requests no longer count missing permissions.
- The README warns to keep the dashboard private when a token feeds it.

## 1.0.0

The first release, for minecraft-exporter 1.0.0.

- **Server:** status, players online, TPS, tick time, heap, uptime, version, and how many players have ever joined.
- **Performance:** TPS over three windows, tick times by percentile with the 50 ms line, the Java heap, CPU, and garbage collection.
- **Worlds:** loaded chunks, entities, block entities, the most common entities, weather, and the day count.
- **Players:** players online and their ping, who's online now with health, food, level, and idle time, who played most in the time range, and a table of every player's lifetime statistics.
- **Activity:** joins, deaths, and advancements over time, deaths by cause and killer, mobs, blocks, distance, new players, and other plugins' events.
- **Chat and events:** tables read straight from WorldAPI through the Infinity data source.
- JVM and exporter rows, folded away.
- Variables for the Prometheus and Infinity data sources, the server, and players, so the dashboard imports from grafana.com and loads from a provisioned file alike.
