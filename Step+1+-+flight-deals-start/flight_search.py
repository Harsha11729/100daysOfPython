import serpapi
from config import flight_search_api,flight_url

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api = flight_search_api
        self.flight_url = flight_url
        self.engine = "google_flights"

    def flight_search(self, departure_id:str, arrival_id:str,date:str,stops:int):
        query = {
            "engine": "google_flights",
            "departure_id": departure_id,
            "arrival_id": arrival_id,
            "currency":"INR",
            "stops":stops,
            "type": 2,
            "outbound_date":date
        }
        client=serpapi.Client(api_key=self.api)
        results=client.search(query)
        print(results.keys())
        print(arrival_id)
        best_flights=results.get('best_flights')
        if not best_flights:
            best_flights=results.get("other_flights")
        return best_flights
