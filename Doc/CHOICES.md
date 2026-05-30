# Engineering Choices Document

## 1. Detection Model Choice

### Options considered:
- YOLOv8
- Faster R-CNN
- RT-DETR

### Final choice: YOLOv8 (nano)

### Why:
- Lightweight and fast on CPU
- Easy integration with OpenCV pipeline
- Good enough accuracy for person detection
- Works well for real-time video processing

### Trade-offs:
- Lower accuracy than transformer-based models
- Limited robustness under heavy occlusion

---

## 2. Event Schema Design

### Options considered:
- Frame-level logging
- Object-level tracking events
- Session-based events

### Final choice: Session + Event hybrid model

### Why:
- Business requires visitor-level analytics
- Supports funnel analysis (entry → purchase)
- Enables re-entry detection and conversion tracking

### Key design decision:
Each visitor is assigned a `visitor_id` per session and tracked across zones.

---

## 3. API Architecture Choice

### Options considered:
- Django REST
- Flask
- FastAPI

### Final choice: FastAPI

### Why:
- High performance async support
- Easy schema validation with Pydantic
- Automatic API docs (Swagger)
- Simple deployment with Uvicorn

---

## 4. AI Usage Decision

### Used AI for:
- Designing event schema structure
- Debugging pipeline architecture issues
- Improving funnel computation logic

### Rejected AI suggestions:
- Fully cloud-based architecture (too complex for assignment scope)
- Heavy Re-ID models (not required for baseline scoring)

---

## 5. Key Engineering Trade-offs

- Chose simplicity over heavy ML models
- In-memory storage instead of DB for speed
- Rule-based funnel logic instead of ML-based attribution