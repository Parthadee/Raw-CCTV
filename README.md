# 📌 Store Intelligence System

An end-to-end computer vision + analytics pipeline that converts raw CCTV footage into real-time retail intelligence using object detection, tracking, event streaming, and a FastAPI analytics engine.

---

## 🚀 Project Overview

Retail stores have very limited visibility into offline customer behavior. This system solves that by converting CCTV video into structured data and computing live business metrics.

It processes raw video, detects people, tracks movement, generates events, and exposes analytics APIs.

---

## 🧠 Key Features

- YOLOv8-based person detection
- Frame-level tracking for visitor sessions
- Event generation (ENTRY, ZONE_ENTER, BILLING_QUEUE, PURCHASE)
- FastAPI backend for real-time analytics
- Funnel and conversion rate computation
- Basic anomaly detection system
- Streamlit dashboard for visualization
- Docker-ready structure

---

## 📁 Project Structure
```
/store-intelligence/
├── pipeline/
│   ├── detect.py          # Main detection + tracking script
│   ├── tracker.py         # Re-ID / tracking logic
│   ├── emit.py            # Event schema + emission
│   └── run.sh             # One command to process all clips → events
├── app/
│   ├── main.py            # FastAPI entrypoint
│   ├── models.py          # Pydantic event schema
│   ├── ingestion.py       # Ingest, dedup
│   ├── metrics.py         # Real-time metric computation
│   ├── funnel.py          # Funnel + session logic
│   ├── anomalies.py       # Anomaly detection
│   └── health.py
├── tests/
│   ├── test_pipeline.py   # Include prompt block header
│   ├── test_metrics.py
│   └── test_anomalies.py
├── docs/
│   ├── DESIGN.md          # Architecture + AI-assisted decisions
│   └── CHOICES.md         # 3 decisions with full reasoning
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/store-intelligence.git
cd store-intelligence

# 🏪 Offline Store Analytics — Computer Vision Pipeline

> Real-time customer behavior tracking and business metric computation using YOLOv8 + FastAPI.

---

# 🏪 Offline Store Analytics — Computer Vision Pipeline

> Real-time customer behavior tracking and business metric computation using YOLOv8 + FastAPI.

---

## 🚀 Getting Started

### 2. Create Virtual Environment

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

### Step 1: Run Detection Pipeline

```bash
python pipeline/detect.py --video "CCTV Footage/entry_cam.mp4" --output output/events.jsonl
```

### Step 2: Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

API runs at: **http://127.0.0.1:8000**

### Step 3: Ingest Events

```bash
python pipeline/replay_events.py --file output/events.jsonl --api http://127.0.0.1:8000/events/ingest
```

### Step 5 *(Optional)*: Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

## 📊 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/events/ingest` | Ingests event batches from detection pipeline |
| `GET` | `/stores/{store_id}/metrics` | Returns entry count, zone visits, billing queue, purchases, conversion rate |
| `GET` | `/stores/{store_id}/funnel` | Returns funnel breakdown: Entry → Zone → Billing → Purchase |
| `GET` | `/stores/{store_id}/heatmap` | Returns zone engagement scores |
| `GET` | `/stores/{store_id}/anomalies` | Detects conversion drops, queue spikes, dead zones |
| `GET` | `/health` | System health check and last event timestamp |

---

## 📈 Core Metric

### Offline Store Conversion Rate
Conversion Rate = (Purchases / Entries) × 100

---

## 🧩 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.12 |
| API Framework | FastAPI |
| Computer Vision | YOLOv8 (Ultralytics) |
| Video Processing | OpenCV |
| Data Validation | Pydantic |
| Dashboard | Streamlit |
| Deployment | Docker |

---

## ⚠️ Limitations

- No deep Re-ID model (simplified tracking)
- In-memory event storage (no database)
- Basic anomaly detection rules
- Simplified zone mapping

---

## 🔮 Future Improvements

- ByteTrack / DeepSORT integration
- PostgreSQL or Kafka pipeline
- Real-time streaming architecture
- Improved re-entry detection
- Multi-store scalability
- Production-grade monitoring

---

## 📌 Author Notes

This project demonstrates an end-to-end system design covering:

- Computer vision pipeline
- Event-driven architecture
- Real-time API design
- Business metric computation

---

## 📜 License

For educational and evaluation purposes only.


