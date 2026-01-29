def write_report(analysis, root_causes, anomaly_msg, recommendations):
    lines = []

    lines.append("📊 AI Ops Incident Analysis Report")
    lines.append("=" * 40)
    lines.append("")

    lines.append("🔹 Issue Breakdown")
    for issue, count in analysis.items():
        lines.append(f"- {issue}: {count} incidents")

    lines.append("")
    lines.append("🔹 Root Cause Analysis")
    for cause, count in root_causes.items():
        lines.append(f"- {cause}: {count} related incidents")

    lines.append("")
    lines.append("🚨 Anomaly Detection")
    lines.append(anomaly_msg)

    lines.append("")
    lines.append("🛠️ Recommended Actions")
    if recommendations:
        for rec in recommendations:
            lines.append(f"- {rec}")
    else:
        lines.append("No immediate action required")

    return "\n".join(lines)
