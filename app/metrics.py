def calculate_metrics(events, store_id):

    filtered = [
        e for e in events
        if e["store_id"] == store_id
    ]

    entry = sum(1 for e in filtered if e["event_type"] == "ENTRY")
    zone = sum(1 for e in filtered if e["event_type"] == "ZONE_ENTER")
    billing = sum(1 for e in filtered if e["event_type"] == "BILLING_QUEUE_JOIN")
    purchase = sum(1 for e in filtered if e["event_type"] == "PURCHASE")

    conversion_rate = (purchase / entry * 100) if entry > 0 else 0

    return {
        "store_id": store_id,
        "entry": entry,
        "zone": zone,
        "billing": billing,
        "purchase": purchase,
        "conversion_rate": round(conversion_rate, 2)
    }