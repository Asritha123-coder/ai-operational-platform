def find_root_causes(tickets):
    causes = {
        "Authentication Service": ["login", "auth"],
        "Database": ["database", "timeout"],
        "Performance": ["slow", "latency"]
    }

    root_cause_count = {}

    for ticket in tickets:
        text = ticket.lower()
        for cause, keywords in causes.items():
            if any(word in text for word in keywords):
                root_cause_count[cause] = root_cause_count.get(cause, 0) + 1

    return root_cause_count
