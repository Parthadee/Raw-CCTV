import json
import requests
import argparse
import os
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--file", required=True)
parser.add_argument("--api", required=True)

args = parser.parse_args()

# Check if event file exists
if not os.path.exists(args.file):
    print(f"ERROR: Event file not found: {args.file}")
    sys.exit(1)

events = []

with open(args.file, "r") as f:
    for line in f:
        line = line.strip()

        if line:
            events.append(json.loads(line))

if len(events) == 0:
    print("WARNING: No events found in file")
    sys.exit(0)

print(f"Loaded {len(events)} events")

BATCH_SIZE = 500

for i in range(0, len(events), BATCH_SIZE):

    batch = events[i:i + BATCH_SIZE]

    try:

        response = requests.post(
            args.api,
            json=batch,
            timeout=30
        )

        print(
            f"Batch {i // BATCH_SIZE + 1}: "
            f"{response.status_code}"
        )

        try:
            print(response.json())
        except:
            print(response.text)

    except requests.exceptions.ConnectionError:

        print(
            f"ERROR: Cannot connect to API: {args.api}"
        )

        print(
            "Start FastAPI first using:"
        )

        print(
            "uvicorn app.main:app --reload"
        )

        sys.exit(1)

    except Exception as e:

        print(
            f"ERROR: {e}"
        )

        sys.exit(1)

print("All events uploaded successfully")