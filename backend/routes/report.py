from flask import Blueprint, jsonify
from services.ticket_parser import parse_tickets
from services.analyzer import analyze_tickets
from services.root_cause import find_root_causes
from services.anomaly_detector import detect_anomaly
from services.recommendation_engine import generate_recommendations
from services.ai_writer import write_report
from services.llm_writer import generate_ai_report

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["GET"])
def generate_report():
    tickets = parse_tickets()
    analysis = analyze_tickets(tickets)
    root_causes = find_root_causes(tickets)
    is_anomaly, anomaly_msg = detect_anomaly(tickets)
    recommendations = generate_recommendations(analysis, root_causes)

    ai_report = generate_ai_report(
        analysis,
        root_causes,
        anomaly_msg,
        recommendations
    )

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
