from tkinter import *
COLOR = '#A7ECEE'


class NotificationManager:
    def __init__(self,name, currency, details):

        def destroy():
            window.destroy()

        window = Tk()
        window.config(padx=50, pady=50, bg=COLOR)
        window.title('Cheap flight finder')

        label = Label(text=f'Dear {name}, cheapest flight found!!!', bg=COLOR)
        label.grid(row=0, column=0, sticky='w', pady=10)

        from_label = Label(text='From:', bg=COLOR)
        from_label.grid(row=1, column=0, sticky='w')
        from_location = Label(text=f'{details["from"]}', bg=COLOR)
        from_location.grid(row=1, column=1, sticky='w')

        to_label = Label(text='To:', bg=COLOR)
        to_label.grid(row=2, column=0, sticky='w')
        to_location = Label(text=f'{details["to"]}', bg=COLOR)
        to_location.grid(row=2, column=1, sticky='w')

        cost_label = Label(text='Cost:', bg=COLOR)
        cost_label.grid(row=3, column=0, sticky='w')
        cost_var = Label(text=f'{currency}{details["price"]}', bg=COLOR)
        cost_var.grid(row=3, column=1, sticky='w')

        airline_label = Label(text='Airline:', bg=COLOR)
        airline_label.grid(row=4, column=0, sticky='w')
        airline_var = Label(text=f'{details["airline"]}', bg=COLOR)
        airline_var.grid(row=4, column=1, sticky='w')

        pnr_label = Label(text='no of person:', bg=COLOR)
        pnr_label.grid(row=5, column=0, sticky='w')
        pnr_var = Label(text=f'{details["no_of_person"]}', bg=COLOR)
        pnr_var.grid(row=5, column=1, sticky='w')

        date_label = Label(text='Date:', bg=COLOR)
        date_label.grid(row=6, column=0, sticky='w')
        date_var = Label(text=f'{details["departure_date"]}', bg=COLOR)
        date_var.grid(row=6, column=1, sticky='w')

        dtime_label = Label(text='Departure time:', bg=COLOR)
        dtime_label.grid(row=7, column=0, sticky='w')
        dtime_var = Label(text=f'{details["departure_time"]}',bg=COLOR)
        dtime_var.grid(row=7, column=1, sticky='w')

        atime_label = Label(text='Arrival time:', bg=COLOR)
        atime_label.grid(row=8, column=0, sticky='w')
        atime_var = Label(text=f'{details["arrival_time"]}', bg=COLOR)
        atime_var.grid(row=8, column=1, sticky='w')

        seat_label = Label(text='Available seat:', bg=COLOR)
        seat_label.grid(row=9, column=0, sticky='w')
        seat_availability = Label(text=f'{details["available_seat"]}', bg=COLOR)
        seat_availability.grid(row=9, column=1, sticky='w')

        button = Button(text='Ok', command=destroy)
        button.grid(row=10, column=0, columnspan=2)

        window.mainloop()
