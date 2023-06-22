# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from ui import Ui
from tkinter import messagebox as mb


def flight_finder():
    search_data = Ui()
    flight_data = FlightData(locations=search_data.location, start=search_data.start_date, stop=search_data.stop_date,
                             persons=search_data.no_of_person, cabin=search_data.cabin, currency=search_data.currency)

    flight_search = FlightSearch(flight_data.conditions)
    notification_manager = NotificationManager(search_data.name, flight_data.currency_abb,
                                               flight_search.processed_details)


is_on = True
while is_on:
    try:
        flight_finder()

    except:
        retry = mb.askyesno('Error', 'There seem to be an error while searching...\n Do you want to retry')
        if not retry:
            is_on = False
