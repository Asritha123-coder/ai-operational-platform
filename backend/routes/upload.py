from flask import Blueprint, request, jsonify
from storage.csv_loader import load_tickets_from_csv
from storage.tickets_store import save_tickets, clear_tickets

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload-tickets", methods=["POST"])
def upload_tickets():
    # 1. Check file exists
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    # 2. Load tickets from CSV
    tickets = load_tickets_from_csv(file.stream)

    # 3. Save tickets
    clear_tickets()
    save_tickets(tickets)

    return jsonify({
        "message": "Tickets uploaded successfully",
        "count": len(tickets)
    })
