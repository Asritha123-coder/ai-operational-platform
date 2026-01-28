def write_report(analysis, root_causes, anomaly_msg):
    report = "📊 AI Ops Summary Report\n\n"

    report += "🔹 Issue Breakdown:\n"
    for issue, count in analysis.items():
        report += f"- {issue}: {count}\n"

    report += "\n🔹 Root Cause Analysis:\n"
    for cause, count in root_causes.items():
        report += f"- {cause}: {count}\n"

    report += "\n🚨 Anomaly Detection:\n"
    report += anomaly_msg

    return report
