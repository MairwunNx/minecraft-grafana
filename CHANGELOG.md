# Changelog

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
