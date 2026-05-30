from fastapi import FastAPI
from typing import List

from .models import Event
from .metrics import calculate_metrics

app = FastAPI()

EVENTS = []


@app.post("/events/ingest")
def ingest(events: List[Event]):
    for e in events:
        EVENTS.append(e.dict())
    return {"status": "ok", "count": len(events)}


@app.get("/stores/{store_id}/metrics")
def metrics(store_id: str):
    return calculate_metrics(EVENTS, store_id)