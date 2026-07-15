---
tags:
  - run.configuration.exec
  - writerside
  - save-as-zip
---

# event:run.configuration.exec:save-as-zip

[TOC]

## Overview

`run.configuration.exec` events are emitted by the JetBrains IDE when a user executes a run configuration. They are the primary telemetry signal for understanding build, test, and deployment activities within the IDE. This documentation focuses on logs from building HTML documentation using the Writerside plugin.

For Writerside (JetBrains' technical documentation plugin), the `run.configuration.exec` events capture the lifecycle of doc builds: when a user initiates a build (`started` event), when the UI appears (`ui.shown`), and when execution completes (`finished` event).

!!! info "Catalog entry for internal analytics use"
    This page documents the Writerside-specific `run.configuration.exec` events as observed in JetBrains telemetry logs (`fus.log`). The run configuration factory is `save-as-zip`, representing the standard "Build Documentation" action.

---

## Event Log Sample

The following payloads are taken from an actual Writerside telemetry session and illustrate a user building documentation in HTML format and saving it in a ZIP archive.

!!! info "Info"
    The example FUS logs are formatted. The original logs are in JSONL format.

=== "started"

    ```json hl_lines="8 12 17 18"
    {
      "recorder_version": "76",
      "session": "26071007-03f17193a243",
      "build": "261.25134.95",
      "bucket": "247",
      "time": 1783667744739,
      "group": {
        "id": "run.configuration.exec",
        "version": "79"
      },
      "event": {
        "id": "started",
        "count": 1,
        "data": {
          "system_event_id": 28,
          "ide_activity_id": 17,
          "factory": "save-as-zip",
          "plugin": "com.jetbrains.writerside",
          "plugin_version": "2026.06.8817",
          "plugin_type": "JB_NOT_BUNDLED",
          "executor": "Run",
          "id": "StardustRunConfiguration",
          "is_running_current_file": false,
          "is_rerun": false,
          "service_view": false,
          "dumb": false,
          "created": 1783667744739,
          "auto_license_type": "N",
          "project": "5d686409c8c2fc70b456855095277389a6a771d4b8bef6a64f14fd9d39572a87"
        }
      }
    }
    ```

=== "ui.shown"

    ```json hl_lines="8 12"
    {
      "recorder_version": "76",
      "session": "26071007-03f17193a243",
      "build": "261.25134.95",
      "bucket": "247",
      "time": 1783667744831,
      "group": {
        "id": "run.configuration.exec",
        "version": "79"
      },
      "event": {
        "id": "ui.shown",
        "count": 1,
        "data": {
          "system_event_id": 29,
          "ide_activity_id": 17,
          "created": 1783667744831,
          "auto_license_type": "N",
          "project": "5d686409c8c2fc70b456855095277389a6a771d4b8bef6a64f14fd9d39572a87"
        }
      }
    }
    ```

=== "finished"

    ```json hl_lines="8 12 18"
    {
      "recorder_version": "76",
      "session": "26071007-03f17193a243",
      "build": "261.25134.95",
      "bucket": "247",
      "time": 1783667745170,
      "group": {
        "id": "run.configuration.exec",
        "version": "79"
      },
      "event": {
        "id": "finished",
        "count": 1,
        "data": {
          "system_event_id": 37,
          "ide_activity_id": 17,
          "duration_ms": 431,
          "finish_type": "UNKNOWN",
          "created": 1783667745170,
          "auto_license_type": "N",
          "project": "5d686409c8c2fc70b456855095277389a6a771d4b8bef6a64f14fd9d39572a87"
        }
      }
    }
    ```

---

## Schema Reference

### Event Metadata

!!! info "Info"
  The event metadata represents the first 8 data records of the log line. The IDE collects the same metadata for all events. Thus, the number and names of the fields in the metadata are always the same, unlike the event data, where each event has specific metrics.

| Field | Type | Description |
|---|---|---|
| `recorder_version` | `string` | Version of the FUS recorder embedded in the IDE build. |
| `session` | `string` | Session identifier. Format: `YYMMDD##-<random>`. |
| `build` | `string` | IDE build number (e.g. `261.25134.95`). |
| `bucket` | `string` | A/B bucket assignment. |
| `time` | `int64` | Timestamp of the event in milliseconds. |
| `group.id` | `string` | Event group identifier. Always `"run.configuration.exec"` for Writerside documentation build events. |
| `group.version` | `int` | Version of the event group. |
| `event.id` | `string` | Event stage identifier. One of `"started"`, `"ui.shown"`, `"finished"` for Writerside builds. |
| `event.count` | `int` | Aggregation counter. Usually `1`. |

### `event.data` fields — `started`

| Field | Type | Description |
|---|---|---|
| `system_event_id` | `int` | Numeric event ID. The number sequentially increases within the session. |
| `ide_activity_id` | `int` | Unique ID linking all stages of a single execution (`started`→`ui.shown`→`finished`). |
| `factory` | `string` | Run configuration factory identifier. For Writerside: `"save-as-zip"` (HTML documentation build). |
| `plugin` | `string` | Plugin ID originating the run configuration. For Writerside: `"com.jetbrains.writerside"`. |
| `plugin_version` | `string` | Version of the Writerside plugin (e.g. `"2026.06.8817"`). |
| `plugin_type` | `string` | Always `"JB_NOT_BUNDLED"` for Writerside (separately installed). |
| `executor` | `string` | The executor type. Typically `"Run"` for Writerside builds. |
| `id` | `string` | The run configuration ID. For Writerside: `"StardustRunConfiguration"`. |
| `is_running_current_file` | `bool` | Whether the build is scoped to the currently active file only. |
| `is_rerun` | `bool` | Whether this is a re-execution of a previously run configuration. |
| `service_view` | `bool` | Whether the execution UI is shown in a Services tool window. |
| `dumb` | `bool` | Whether the IDE was in dumb mode (indexing in progress) at start. |
| `created` | `int64` | Timestamp in milliseconds when this event record was created. |
| `auto_license_type` | `string` | License type that the IDE uses. |
| `project` | `string` | SHA-256 hash of the project path. **Anonymized** — cannot be reversed to a real path. |

### `event.data` fields — `ui.shown`

| Field | Type | Description |
|---|---|---|
| `system_event_id` | `int` | Numeric event ID. The number sequentially increases within the session. |
| `ide_activity_id` | `int` | Unique ID linking all stages of a single execution (`started`→`ui.shown`→`finished`). |
| `created` | `int64` | Timestamp in milliseconds when the UI appeared. |
| `auto_license_type` | `string` | License type that the IDE uses. |
| `project` | `string` | SHA-256 hash of the project path. **Anonymized**. |

### `event.data` fields — `finished`

| Field | Type | Description |
|---|---|---|
| `system_event_id` | `int` | Numeric event ID. The number sequentially increases within the session. |
| `ide_activity_id` | `int` | Unique ID linking all stages of a single execution (`started`→`ui.shown`→`finished`). |
| `duration_ms` | `int` | Total elapsed time in milliseconds from `started` to `finished`. |
| `finish_type` | `string` | The outcome type. Common values: `"UNKNOWN"`, `"SUCCESS"`, `"ERROR"`, `"STOPPED"`. |
| `created` | `int64` | Timestamp in milliseconds when the execution finished. |
| `auto_license_type` | `string` | License type that the IDE uses. |
| `project` | `string` | SHA-256 hash of the project path. **Anonymized**. |

## Analytics example: How long do Writerside builds take?

To measure average Writerside build durations, first identify Writerside runs in `started` events (`plugin == "com.jetbrains.writerside"` and `factory == "save-as-zip"`), then collect matching `finished` events by `session + ide_activity_id` and calculate duration metrics.

=== "Python"

    ```python linenums="1" hl_lines="12-15 20-21 23"
    import json

    writerside_runs = set()
    durations = []

    with open("fus.log") as f:
        for line in f:
            event = json.loads(line)
            data = event["event"]["data"]

            if (
                event["group"]["id"] == "run.configuration.exec"
                and event["event"]["id"] == "started"
                and data.get("plugin") == "com.jetbrains.writerside"
                and data.get("factory") == "save-as-zip"
            ):
                writerside_runs.add((event.get("session"), data.get("ide_activity_id")))

            if (
                event["group"]["id"] == "run.configuration.exec"
                and event["event"]["id"] == "finished"
                and (event.get("session"), data.get("ide_activity_id")) in writerside_runs
                and data.get("finish_type") in {"SUCCESS", "UNKNOWN"}
            ):
                durations.append(data["duration_ms"])

    print(f"Writerside builds: {len(durations)}")
    if durations:
        print(f"Average duration: {sum(durations) / len(durations):.0f} ms")
        print(f"Fastest: {min(durations)} ms")
        print(f"Slowest: {max(durations)} ms")
    else:
        print("No matching finished events found.")
    ```

=== "SQL (DuckDB syntax)"

    ```sql linenums="1"
    WITH writerside_started AS (
        SELECT
          session AS session,
          "event".data.ide_activity_id AS ide_activity_id
        FROM read_ndjson('fus.log', auto_detect=true)
        WHERE "group".id = 'run.configuration.exec'
          AND "event".id = 'started'
          AND "event".data.plugin = 'com.jetbrains.writerside'
          AND "event".data.factory = 'save-as-zip'
    )
    SELECT
        COUNT(*)                    AS writerside_builds,
        AVG(f."event".data.duration_ms) AS avg_duration_ms,
        MIN(f."event".data.duration_ms) AS fastest_ms,
        MAX(f."event".data.duration_ms) AS slowest_ms
    FROM read_ndjson('fus.log', auto_detect=true) AS f
    JOIN writerside_started ws
      ON f.session = ws.session
     AND f."event".data.ide_activity_id = ws.ide_activity_id
    WHERE f."group".id = 'run.configuration.exec'
      AND f."event".id = 'finished'
      AND f."event".data.finish_type IN ('SUCCESS', 'UNKNOWN')
    ```

!!! Comment

    In this task, I used GitHub Copilot to format the FUS logs into a human-readable format.

    The analytics examples are also AI-generated from my idea and with my corrections, as it is much faster that way. I have tested the Python example, and it gives the correct result. I did not test the SQL example because I don't have DuckDB or any other DB deployed on my machine at the moment. The SQL syntax must be adjusted depending on which database JetBrains uses to store collected data. DuckDB seems to be the right choice if you want to query a JSONL file directly for analytics.

---

## Reference

- [Data Sharing](https://www.jetbrains.com/help/idea/settings-usage-statistics.html)
- [Product Data Collection and Usage Notice](https://www.jetbrains.com/legal/docs/terms/product_data_collection/)