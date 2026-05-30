from datetime import datetime, UTC
import json
from pathlib import Path


EVENT_FILE = Path("../output/events.jsonl")


def get_last_event_timestamp():

    if not EVENT_FILE.exists():
        return None

    last_event = None

    with open(EVENT_FILE, "r", encoding="utf-8") as f:

        for line in f:
            if line.strip():
                last_event = json.loads(line)

    if not last_event:
        return None

    return last_event.get("timestamp")


def get_event_count():

    if not EVENT_FILE.exists():
        return 0

    with open(EVENT_FILE, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def health():

    now = datetime.now(UTC)

    last_event_time = get_last_event_timestamp()

    stale_feed = False

    if last_event_time:

        try:

            event_time = datetime.fromisoformat(
                last_event_time.replace("Z", "+00:00")
            )

            age_seconds = (
                now - event_time
            ).total_seconds()

            stale_feed = age_seconds > 600

        except Exception:
            stale_feed = True

    response = {
        "status": "UP",
        "timestamp": now.isoformat(),
        "event_count": get_event_count(),
        "last_event_timestamp": last_event_time,
        "stale_feed": stale_feed,
        "stores": {
            "STORE_BLR_001": {
                "status": (
                    "STALE_FEED"
                    if stale_feed
                    else "ACTIVE"
                )
            }
        }
    }

    return response


if __name__ == "__main__":

    result = health()

    print(
        json.dumps(
            result,
            indent=4
        )
    )