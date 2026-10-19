# Changelog

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
