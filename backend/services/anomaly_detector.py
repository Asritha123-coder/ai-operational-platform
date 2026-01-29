def detect_anomaly(tickets, threshold=5):
    """
    Detects anomaly based on ticket volume.
    """
    ticket_count = len(tickets)

    if ticket_count > threshold:
        return True, f"High incident volume detected: {ticket_count} tickets"

    return False, "Incident volume is within normal range"
