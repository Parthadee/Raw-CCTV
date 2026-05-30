import json
import uuid

def emit_event(event):

    event["event_id"] = str(
        uuid.uuid4()
    )

    with open(
        "events.jsonl",
        "a"
    ) as f:

        f.write(
            json.dumps(event)
            + "\n"
        )