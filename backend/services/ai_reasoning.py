from services.gemini_writer import generate_ai_report

def generate_ai_reasoning(risk_score, priority, analysis, anomaly_msg, departments):
    prompt_data = f"""
Risk Score: {risk_score}
Priority: {priority}

Issue Breakdown:
{analysis}

Affected Departments:
{list(departments.keys())}

Anomaly Status:
{anomaly_msg}

Explain clearly why this incident was assigned this priority.
"""

    return generate_ai_report(
        analysis,
        {},
        anomaly_msg,
        [prompt_data]
    )
