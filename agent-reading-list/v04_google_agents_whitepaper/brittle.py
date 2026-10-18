# Hand-written glue code: parse the request yourself, then call the API
import re

def flights_api(origin, destination, date):
    return f"3 flights {origin}->{destination} on {date}"

def glue(request):
    m = re.search(r"from (\w+) to (\w+) on (\d+ \w+)", request)
    return flights_api(*m.groups())          # breaks if any part is missing

if __name__ == "__main__":
    for r in ["Flights from Chennai to Pune on 5 Nov",
              "I want to fly to Delhi on 8 Nov"]:
        try:
            print("OK:   ", glue(r))
        except Exception as e:
            print("CRASH:", type(e).__name__, "for:", r)
