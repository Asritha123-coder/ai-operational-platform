def compute_risk_score(tickets_count, anomaly_detected, department_count):
    """
    Computes AI-style risk score (0–100)
    """

    score = 0

    # Volume impact
    if tickets_count > 1000:
        score += 40
    elif tickets_count > 300:
        score += 25
    else:
        score += 10

    # Anomaly impact
    if anomaly_detected:
        score += 40

    # Department impact
    if department_count >= 3:
        score += 20
    elif department_count == 2:
        score += 10

    return min(score, 100)


def classify_risk(score):
    if score >= 80:
        return "CRITICAL", "P1"
    elif score >= 50:
        return "HIGH", "P2"
    else:
        return "MODERATE", "P3"
