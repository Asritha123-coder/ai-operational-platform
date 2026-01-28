from collections import Counter

def analyze_tickets(tickets):
    keywords = {
        "login": "Login Issues",
        "slow": "Performance Issues",
        "timeout": "Database Issues",
        "database": "Database Issues"
    }

    counts = Counter()

    for ticket in tickets:
        text = ticket.lower()
        for key, label in keywords.items():
            if key in text:
                counts[label] += 1

    return counts
