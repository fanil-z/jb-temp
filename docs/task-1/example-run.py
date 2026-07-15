import json

writerside_runs = set()
durations = []

with open("./data/fus.log") as f:
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

print(f"Writerside builds : {len(durations)}")
print(f"Average duration  : {sum(durations) / len(durations):.0f} ms")
print(f"Fastest           : {min(durations)} ms")
print(f"Slowest           : {max(durations)} ms")