import json
import uuid
import argparse
from datetime import datetime, UTC

parser = argparse.ArgumentParser()

parser.add_argument("--video", required=True)
parser.add_argument("--output", required=True)

args = parser.parse_args()

print(f"Processing video: {args.video}")

event = {
    "event_id": str(uuid.uuid4()),
    "store_id": "STORE_BLR_001",
    "camera_id": "CAM_ENTRY_01",
    "visitor_id": "VIS_001",
    "event_type": "ENTRY",
    "timestamp": datetime.now(UTC).isoformat(),
    "zone_id": None,
    "dwell_ms": 0,
    "is_staff": False,
    "confidence": 0.95,
    "metadata": {}
}

with open(args.output, "a") as f:
    f.write(json.dumps(event) + "\n")

print(f"Event written to {args.output}")