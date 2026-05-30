import json


def detect_anomalies(metrics):

    anomalies = []

    if metrics.get("conversion_rate", 0) < 10:

        anomalies.append({
            "severity": "WARN",
            "type": "CONVERSION_DROP",
            "suggested_action": "Check staffing and queue."
        })

    if metrics.get("queue_depth", 0) > 10:

        anomalies.append({
            "severity": "CRITICAL",
            "type": "BILLING_QUEUE_SPIKE",
            "suggested_action": "Open additional billing counters."
        })

    if metrics.get("dead_zone", False):

        anomalies.append({
            "severity": "INFO",
            "type": "DEAD_ZONE",
            "suggested_action": "Review store layout and promotions."
        })

    return anomalies


if __name__ == "__main__":

    metrics = {
        "conversion_rate": 5,
        "queue_depth": 15,
        "dead_zone": True
    }

    print(json.dumps(
        detect_anomalies(metrics),
        indent=4
    ))