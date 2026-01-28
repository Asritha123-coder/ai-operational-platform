from flask import Blueprint, request, jsonify
from storage.csv_loader import load_tickets_from_csv
from storage.tickets_store import save_tickets, clear_tickets

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload-tickets-raw", methods=["POST"])
def upload_tickets_raw():
    raw_data = request.data.decode("utf-8")

    if not raw_data:
        return {"error": "No data received"}, 400

    lines = raw_data.splitlines()
    tickets = lines[1:]  # skip header

    clear_tickets()
    save_tickets(tickets)

    return {
        "message": "Tickets uploaded via raw data",
        "count": len(tickets)
    }

