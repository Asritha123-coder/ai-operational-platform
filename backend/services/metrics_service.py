def build_metrics(analysis, root_causes, is_anomaly):
    metrics = {}

    metrics["total_incidents"] = sum(analysis.values())

    metrics["top_issue"] = (
        max(analysis, key=analysis.get) if analysis else "None"
    )

    metrics["top_root_cause"] = (
        max(root_causes, key=root_causes.get) if root_causes else "None"
    )

    metrics["anomaly_detected"] = is_anomaly

    return metrics
