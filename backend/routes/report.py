from flask import Blueprint, jsonify
from services.ticket_parser import parse_tickets
from services.analyzer import analyze_tickets
from services.ai_writer import write_report
from services.root_cause import find_root_causes
from services.anomaly_detector import detect_anomaly

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["GET"])
def generate_report():
    tickets = parse_tickets()
    analysis = analyze_tickets(tickets)

    root_causes = find_root_causes(tickets)
    is_anomaly, anomaly_msg = detect_anomaly(tickets)

    report = write_report(
        analysis=analysis,
        root_causes=root_causes,
        anomaly_msg=anomaly_msg
    )

    return jsonify({"report": report})
