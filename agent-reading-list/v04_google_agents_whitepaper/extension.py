# An Extension: teach the agent an API with an example and required
# parameters. The agent itself calls the API (agent-side execution).
import json
from mini_llm import call_model
from brittle import flights_api

FLIGHTS_EXT = {"name": "flights",
               "required": ["origin", "destination", "date"],
               "example": "Flights from Chennai to Pune on 5 Nov -> "
                          "origin=Chennai, destination=Pune, date=5 Nov"}

def agent(request):
    args = json.loads(call_model("fill_args", request, ext=FLIGHTS_EXT))
    missing = [p for p in FLIGHTS_EXT["required"] if not args[p]]
    if missing:
        return f"Agent asks: what is your {missing[0]} city?"
    return "Agent calls API: " + flights_api(**args)

for r in ["I want to fly to Delhi on 8 Nov",
          "Fly from Hyderabad to Delhi on 8 Nov"]:
    print(agent(r))
