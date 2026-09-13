from flight_search import FlightSearch
class FlightData:
    def find_cheapest_flights(self,flights):
        if not flights:
            return None
        cheapest=flights[0]
        return {
            "price":cheapest["price"],
            "airline": cheapest["flights"][0]["airline"],
            "departure": cheapest["flights"][0]["departure_airport"]["id"],
            "arrival": cheapest["flights"][0]["arrival_airport"]["id"],
            "departure_time": cheapest["flights"][0]["departure_airport"]["time"],
            "arrival_time": cheapest["flights"][0]["arrival_airport"]["time"]

        }
flight_data=FlightData()
flight_search=FlightSearch()
print(flight_data.find_cheapest_flights(flight_search.flight_search("HYD","VTZ","2026-06-10","1")))
print()
