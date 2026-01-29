from flask import Blueprint, jsonify
from services.ticket_parser import parse_tickets
from services.analyzer import analyze_tickets
from services.root_cause import find_root_causes
from services.anomaly_detector import detect_anomaly
from services.recommendation_engine import generate_recommendations
from services.ai_writer import write_report

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["GET"])
def generate_report():
    # 1. Get tickets
    tickets = parse_tickets()

    # 2. Analyze issues
    analysis = analyze_tickets(tickets)

    # 3. Root cause analysis (DEFINE FIRST)
    root_causes = find_root_causes(tickets)

    # 4. Anomaly detection
    is_anomaly, anomaly_msg = detect_anomaly(tickets)

    # 5. Generate recommendations (NOW SAFE)
    recommendations = generate_recommendations(analysis, root_causes)

    # 6. Generate report
    report = write_report(
        analysis=analysis,
        root_causes=root_causes,
        anomaly_msg=anomaly_msg,
        recommendations=recommendations
    )

    return jsonify({"report": report})
