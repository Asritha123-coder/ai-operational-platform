from storage.tickets_store import get_all_tickets

def parse_tickets():
    tickets = get_all_tickets()
    print("TICKETS IN STORE:", tickets)  # 👈 debug
    return tickets
