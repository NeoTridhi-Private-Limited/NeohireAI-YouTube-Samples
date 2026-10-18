# API-Bank idea: first find the right API, then call it
APIS = {
    "get_balance": ("check the balance of a bank account",
                    lambda: "Rs 12,400"),
    "book_appointment": ("book a doctor appointment at a hospital",
                         lambda: "booked for 10:30"),
    "track_parcel": ("track where a parcel or delivery is now",
                     lambda: "out for delivery"),
}

def search_api(request):                  # an API search engine
    words = set(request.lower().split())
    return max(APIS, key=lambda n: len(words & set(APIS[n][0].split())))

for req in ["Where is my parcel now", "Book a doctor appointment Monday",
            "What is the balance in my account"]:
    name = search_api(req)
    print(f"{req:<34} -> {name}() -> {APIS[name][1]()}")
