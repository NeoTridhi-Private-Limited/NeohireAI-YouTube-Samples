"""travel_tools.py - stand-in travel APIs used by react_loop.py and concierge.py (no network)."""
TRAINS = {"HYD-BLR": [("T101", "3A", 1450), ("T205", "3A", 2100), ("T330", "2A", 2650)]}
SEATS = {"T101": 12, "T205": 40, "T330": 6}

def search_trains(route):                      # agent side: the agent calls this itself
    return "; ".join(f"{n} {c} {p}" for n, c, p in TRAINS.get(route, [])) or "no trains"

def check_seats(train):
    return f"{SEATS[train]} seats left"

def book_ticket_ui(train, confirm):            # client side: the app runs it, after the user says yes
    return f"booked {train}, PNR 4521" if confirm else "user declined"
