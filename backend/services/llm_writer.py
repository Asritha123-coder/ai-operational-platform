def generate_ai_report(analysis, root_causes, anomaly_msg, recommendations):
    """
    This simulates an LLM-generated report.
    Later this can be replaced by OpenAI / Gemini / Ollama.
    """

    report = (
        "Executive Incident Summary\n\n"
        f"Issues detected: {dict(analysis)}\n"
        f"Root causes identified: {dict(root_causes)}\n"
        f"Anomaly status: {anomaly_msg}\n"
        f"Recommended actions: {recommendations}\n\n"
        "Overall system requires attention in the highlighted areas."
    )

    return report
