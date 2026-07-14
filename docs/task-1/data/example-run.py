import json

durations = []

with open("fus.log") as f:
    for line in f:
        event = json.loads(line)
        data = event["event"]["data"]
        if (
            event["group"]["id"] == "run.configuration.exec"
            and event["event"]["id"] == "finished"
            and data.get("finish_type") == "UNKNOWN"
        ):
            durations.append(data["duration_ms"])

print(f"Successful builds : {len(durations)}")
print(f"Average duration  : {sum(durations) / len(durations):.0f} ms")
print(f"Fastest           : {min(durations)} ms")
print(f"Slowest           : {max(durations)} ms")