from flask import Blueprint, jsonify

from services.ticket_parser import parse_tickets
from services.analyzer import analyze_tickets
from services.root_cause import find_root_causes
from services.anomaly_detector import detect_anomaly
from services.recommendation_engine import generate_recommendations
from services.ai_writer import write_report
from services.gemini_writer import generate_ai_report   # ✅ Gemini AI

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["GET"])
def generate_report():
    # 1. Load tickets
    tickets = parse_tickets()

    # 2. Analysis
    analysis = analyze_tickets(tickets)
    root_causes = find_root_causes(tickets)
    is_anomaly, anomaly_msg = detect_anomaly(tickets)

    # 3. Recommendations
    recommendations = generate_recommendations(analysis, root_causes)

    # 4. AI report (Gemini)
    ai_report = generate_ai_report(
        analysis,
        root_causes,
        anomaly_msg,
        recommendations
    )

    # 5. Response
    return jsonify({
        "structured_report": write_report(
            analysis,
            root_causes,
            anomaly_msg,
            recommendations
        ),
        "ai_report": ai_report,
        "recommendations": recommendations
    })
