# Store Intelligence System – Design Document

## 1. Overview

This system converts raw CCTV video streams into structured retail intelligence. It detects people in video feeds, tracks movement across store zones, generates structured behavioral events, and exposes real-time analytics through a FastAPI service.

The goal is to estimate offline store performance metrics similar to online analytics systems.

---

## 2. System Architecture

The pipeline is divided into four layers:

### 1. Detection Layer (`pipeline/`)
- Input: raw CCTV video clips
- Uses YOLOv8 for person detection
- Tracks objects across frames (simple ID or tracking logic)
- Converts detections into structured events
- Outputs JSONL event stream

### 2. Event Layer
- Normalizes detection outputs into a fixed schema
- Ensures consistency across cameras and stores
- Emits events like ENTRY, ZONE_ENTER, BILLING_QUEUE_JOIN

### 3. API Layer (`app/`)
Built using FastAPI:
- `/events/ingest` → receives event streams
- `/stores/{id}/metrics` → computes live KPIs
- `/stores/{id}/funnel` → conversion funnel
- `/stores/{id}/heatmap` → zone analysis
- `/stores/{id}/anomalies` → operational alerts
- `/health` → system status

### 4. Dashboard (optional)
- Streamlit-based real-time visualization
- Displays conversion rate and store metrics

---

## 3. Data Flow

Video → YOLO Detection → Tracking → Event Generator → JSONL → API Ingestion → Metrics Engine → Dashboard

---

## 4. Storage Strategy

- In-memory event storage (prototype level)
- Designed to be replaced by PostgreSQL or Kafka in production

---

## 5. Key Design Decisions

- Stateless API (events are source of truth)
- Batch ingestion supported (up to 500 events)
- Store filtering done at query level
- Event-driven architecture instead of frame-driven processing

---

## 6. Limitations

- No deep Re-ID model implemented (simplified visitor tracking)
- No persistent DB layer in current version
- Detection accuracy depends on YOLO baseline model