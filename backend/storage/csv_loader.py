import csv

def load_tickets_from_csv(file_stream):
    decoded = file_stream.read().decode("utf-8-sig").splitlines()
    reader = csv.DictReader(decoded)

    tickets = []

    for row in reader:
        text = row.get("ticket_description")
        if text and text.strip():
            tickets.append(text.strip())

    return tickets
