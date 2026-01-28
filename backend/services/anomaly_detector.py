def detect_anomaly(tickets, threshold=5):
    if len(tickets) > threshold:
        return True, f"High incident volume detected: {len(tickets)} tickets"
    return False, "Incident volume is within normal range"
