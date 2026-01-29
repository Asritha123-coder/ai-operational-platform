from flask import Blueprint, jsonify
from services.ticket_parser import parse_tickets
from services.analyzer import analyze_tickets
from services.root_cause import find_root_causes
from services.anomaly_detector import detect_anomaly
from services.metrics_service import build_metrics

metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics", methods=["GET"])
def get_metrics():
    tickets = parse_tickets()

    analysis = analyze_tickets(tickets)
    root_causes = find_root_causes(tickets)
    is_anomaly, _ = detect_anomaly(tickets)

    metrics = build_metrics(analysis, root_causes, is_anomaly)

    return jsonify(metrics)
