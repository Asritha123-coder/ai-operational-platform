# simple in-memory ticket storage
TICKETS = []

def save_tickets(tickets):
    global TICKETS
    TICKETS.extend(tickets)

def get_all_tickets():
    return TICKETS

def clear_tickets():
    global TICKETS
    TICKETS = []
