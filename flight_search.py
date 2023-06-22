import os
import json
import requests
from datetime import datetime


SEARCH_ENDPOINT = 'https://api.tequila.kiwi.com/v2/search'
AIRLINE_ENDPOINT = 'https://api.api-ninjas.com/v1/airlines'
FLIGHT_KEY = os.environ.get('flight_key')
AIRLINE_KEY = os.environ.get('airlines_key')

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, parameter):
        self.parameters = parameter
        self.flight_search = self.search()
        iata_code = self.flight_search[0]
        details = self.flight_search[1]
        self.processed_details = self.find_airline(flight_code=iata_code, cheapest_flight=details)

    def search(self):

        parameters = self.parameters
        header = {
            'apikey': FLIGHT_KEY
        }

        response = requests.get(url=SEARCH_ENDPOINT, params=parameters, headers=header)
        response.raise_for_status()

        data = response.json()

        searched_list = data['data']
        cheapest = min(searched_list, key=lambda x: x['price'])
        flight_iata = cheapest['airlines'][0]
        return flight_iata, cheapest

        # json_object = json.dumps(cheapest, indent=4)
        # print(json_object)
        # for item in searched_list:
        #     if item['price'] < cheapest['price']:
        #         cheapest = item
        #
        # flight_iata = cheapest['airlines'][0]
        # return flight_iata, cheapest

    def find_airline(self, flight_code, cheapest_flight):

        airlines_parameter = {
            'iata': flight_code
        }
        airlines_header = {'X-Api-key': AIRLINE_KEY}

        airline_response = requests.get(url=AIRLINE_ENDPOINT, params=airlines_parameter, headers=airlines_header)
        airline_response.raise_for_status()
        airline_data = airline_response.json()
        airline_name = airline_data[0]['name']

        time = [cheapest_flight['local_departure'], cheapest_flight['local_arrival']]
        formatted_cal = []

        for i in time:
            date_time = datetime.strptime(i, "%Y-%m-%dT%H:%M:%S.%fZ")
            date = date_time.date()
            f_time = date_time.time()

            item = {
                'date': date.strftime('%Y-%m-%d'),
                'time': f_time.strftime('%I:%M:%S %p')
            }
            formatted_cal.append(item)

        price = str(int((cheapest_flight['price'])))
        if len(price) > 3:
            price = price[:-3] + ',' + price[-3:]

        info = {
            'from': f'{cheapest_flight["cityFrom"]}({cheapest_flight["flyFrom"]})',
            'to': f'{cheapest_flight["cityTo"]}({cheapest_flight["flyTo"]})',
            'price': price,
            'no_of_person': cheapest_flight['pnr_count'],
            'airline': airline_name,
            'departure_date': formatted_cal[0]['date'],
            'departure_time': formatted_cal[0]['time'],
            'arrival_time': formatted_cal[1]['time'],
            'available_seat': cheapest_flight['availability']['seats']
        }

        return info
