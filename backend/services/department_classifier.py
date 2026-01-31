from collections import Counter

def classify_by_department(tickets):
    rules = {
        "Authentication": ["login", "auth", "token", "password"],
        "Database": ["database", "db", "query", "timeout"],
        "Performance": ["slow", "latency", "performance"],
        "Network": ["network", "dns", "connection"],
        "Infrastructure": ["server", "cpu", "memory", "disk"]
    }

    counts = Counter()

    for ticket in tickets:
        text = ticket.lower()
        for dept, keywords in rules.items():
            if any(k in text for k in keywords):
                counts[dept] += 1

    return dict(counts)
