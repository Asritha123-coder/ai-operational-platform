import csv

def load_tickets_from_csv(file_stream):
    tickets = []

    decoded = file_stream.read().decode("utf-8").splitlines()
    reader = csv.DictReader(decoded)

    for row in reader:
        # assume CSV column name = description
        tickets.append(row["description"])

    return tickets
