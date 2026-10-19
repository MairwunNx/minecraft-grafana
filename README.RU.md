# Дашборд Minecraft для Grafana

<p align="center">
  <a href="https://grafana.com/grafana/dashboards/GRAFANA_ID"><img alt="grafana.com" src="https://img.shields.io/badge/grafana.com-GRAFANA_ID-F46800?logo=grafana&logoColor=white"></a>
  <a href="https://github.com/MairwunNx/minecraft-grafana/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/MairwunNx/minecraft-grafana?label=release"></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/MairwunNx/minecraft-grafana"></a>
</p>

📈 Дашборд Grafana для сервера Minecraft: как быстро он тикает, чем заполнены миры, кто играет и что делает, и чат. Он рисует метрики [minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter), который читает сервер через [WorldAPI](https://github.com/MairwunNx/minecraft-worldapi).

[English version](README.md)

![Дашборд](media/dashboard.png)

## Что на нём

- 🟢 **Сервер одним взглядом:** работает ли он, игроки онлайн, TPS, время тика, куча, аптайм, версия.
- ⏱️ **Производительность:** TPS, время тика по перцентилям рядом с линией 50 мс, за которой сервер начинает лагать, куча, CPU, сборка мусора.
- 🌍 **Миры:** загруженные чанки, сущности, блочные сущности, самые частые сущности, погода, номер дня.
- 🧑‍🤝‍🧑 **Игроки:** кто онлайн, с здоровьем, сытостью, уровнем и пингом; кто больше всех играл за выбранный период; пожизненная статистика каждого: время в игре, последний заход, достижения, смерти, мобы, блоки, алмазы, пройденный путь, опыт.
- 💀 **Активность:** входы, смерти и достижения во времени, смерти по причинам и убийцам, новые игроки и события других плагинов, например убийства боссов.
- 💬 **Чат и события** таблицами, прямо из WorldAPI.

Сервер и игроков выбирают вверху, а перезапуски отмечены на всех графиках.

## Установка

Нужны Grafana 11 или новее и Prometheus, который опрашивает [minecraft-exporter](https://github.com/MairwunNx/minecraft-exporter/blob/master/README.RU.md#prometheus).

**С grafana.com.** В Grafana откройте Dashboards → New → Import, введите `GRAFANA_ID` и выберите свой Prometheus.

**Из файла.** Скачайте [`minecraft.json`](https://github.com/MairwunNx/minecraft-grafana/releases/latest/download/minecraft.json) и импортируйте так же, или пусть Grafana загрузит его из папки провижининга: источники данных дашборд выбирает через переменные, так что править его не нужно. Пример такой настройки лежит в [`examples/`](https://github.com/MairwunNx/minecraft-exporter/tree/master/examples) у minecraft-exporter.

### Таблицы чата и событий

Эти две таблицы спрашивают WorldAPI напрямую, через источник данных [Infinity](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/):

1. Установите Infinity: `grafana cli plugins install yesoreyeram-infinity-datasource` или `GF_PLUGINS_PREINSTALL_SYNC=yesoreyeram-infinity-datasource` в Docker.
2. Добавьте источник данных Infinity. Укажите в URL свой WorldAPI, например `http://minecraft:8110/api/v1`, а в аутентификации — «Bearer token» с токеном WorldAPI, у которого есть `events:read`, а для чата ещё и `chat:read`.
3. Выберите его в переменной «WorldAPI» на дашборде.

WorldAPI записывает чат, только если в его конфиге стоит `events.chat: true`. Grafana обращается к WorldAPI со своего сервера, поэтому токен не попадает в браузер. Но читать чат сможет любой, кто открывает дашборд: не показывайте его в публичной Grafana без согласия игроков.

## Посмотреть вживую

Moonlands, мой сервер для хардкорного выживания с друзьями, показывает этот дашборд всем: [minecraft.mairwunnx.com/grafana](https://minecraft.mairwunnx.com/grafana/d/minecraft-worldapi/minecraft).

[![Играйте на Moonlands: чистая ванилла, сложные мобы, ИИ, приваты. minecraft.mairwunnx.com](https://raw.githubusercontent.com/MairwunNx/minecraft-worldapi/master/media/og-adv-image.png)](https://minecraft.mairwunnx.com)

## Лицензия

[MIT](LICENSE).
