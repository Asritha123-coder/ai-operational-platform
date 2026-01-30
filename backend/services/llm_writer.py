def generate_ai_report(analysis, root_causes, anomaly_msg, recommendations):
    """
    Mock LLM writer.
    This simulates an AI-generated executive summary.
    Used as a fallback or when external LLM is disabled.
    """

    report = "Executive Incident Summary\n\n"

    report += "Issues detected:\n"
    for issue, count in analysis.items():
        report += f"- {issue}: {count}\n"

    report += "\nRoot causes identified:\n"
    for cause, count in root_causes.items():
        report += f"- {cause}: {count}\n"

    report += f"\nAnomaly status:\n{anomaly_msg}\n"

    report += "\nRecommended actions:\n"
    for rec in recommendations:
        report += f"- {rec}\n"

    report += (
        "\nOverall assessment:\n"
        "The system shows patterns that require operational attention. "
        "Immediate remediation is advised for highlighted components."
    )

    return report
