import json
from pathlib import Path


def build_funnel(events):
    """
    Build conversion funnel from event stream.
    """

    entry_visitors = set()
    zone_visitors = set()
    billing_visitors = set()
    purchase_visitors = set()

    for event in events:

        visitor_id = event.get("visitor_id")
        event_type = event.get("event_type")

        if not visitor_id:
            continue

        if event_type == "ENTRY":
            entry_visitors.add(visitor_id)

        elif event_type == "ZONE_ENTER":
            zone_visitors.add(visitor_id)

        elif event_type == "BILLING_QUEUE_JOIN":
            billing_visitors.add(visitor_id)

        elif event_type == "PURCHASE":
            purchase_visitors.add(visitor_id)

    entry_count = len(entry_visitors)
    zone_count = len(zone_visitors)
    billing_count = len(billing_visitors)
    purchase_count = len(purchase_visitors)

    funnel = {
        "entry": entry_count,
        "zone": zone_count,
        "billing": billing_count,
        "purchase": purchase_count,
        "dropoff": {
            "entry_to_zone": round(
                ((entry_count - zone_count) / entry_count) * 100, 2
            ) if entry_count else 0,

            "zone_to_billing": round(
                ((zone_count - billing_count) / zone_count) * 100, 2
            ) if zone_count else 0,

            "billing_to_purchase": round(
                ((billing_count - purchase_count) / billing_count) * 100, 2
            ) if billing_count else 0
        }
    }

    return funnel


def load_events(file_path):
    """
    Load events from JSONL file.
    """

    events = []

    path = Path(file_path)

    if not path.exists():
        print(f"File not found: {file_path}")
        return []

    with open(file_path, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            try:
                events.append(json.loads(line))

            except json.JSONDecodeError:
                print(f"Skipping invalid line: {line}")

    return events


if __name__ == "__main__":

    events = load_events("../output/events.jsonl")

    print(f"Loaded {len(events)} events")

    result = build_funnel(events)

    print("\n===== FUNNEL REPORT =====")
    print(json.dumps(result, indent=4))