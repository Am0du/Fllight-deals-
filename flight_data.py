import os
import requests


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, locations, start, stop, persons, cabin, currency):

        if cabin == 'first class':
            select_cabin = 'F'
        elif cabin == 'economy premium':
            select_cabin = 'W'
        elif cabin == 'business':
            select_cabin = 'C'
        else:
            select_cabin = 'M'

        if currency == 'naira':
            currency = 'NGN'
        elif currency == 'euro':
            currency = 'EUR'
        elif currency == 'pounds sterling':
            currency = 'GBP'
        else:
            currency = 'USD'

        from_to = []
        for location in locations:
            location_endpoint = 'https://api.tequila.kiwi.com/locations/query'
            location_key = os.environ.get('flight_key')
            headers = {
                'apikey': location_key
            }
            parameter ={
                'term': location,
            }

            response = requests.get(url=location_endpoint, params=parameter, headers=headers)
            response.raise_for_status()
            data = response.json()
            from_to.append(data['locations'][0]['code'])

        self.currency_abb = currency
        self.conditions = {
            'fly_from': from_to[0],
            'fly_to': from_to[1],
            'date_from': start,
            'date_to': stop,
            'flight_type': 'oneway',
            'one_per_date': 1,
            'adults': persons,
            'selected_cabins': select_cabin,
            'ret_from_diff_city': False,
            'limit': 20,
            'curr': currency

        }