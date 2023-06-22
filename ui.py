from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import date
COLOR = '#A7ECEE'

class Ui:
    def __init__(self):

        self.name = ''
        self.location = []
        self.start_date = ''
        self.stop_date = ''
        self.no_of_person = 1
        self.cabin = ''
        self.currency = ''

        self.ui()

    def ui(self):
        def submit():
            self.name = name_entry.get()
            self.location = [from_entry.get(), to_entry.get()]
            self.start_date = stcal.get()
            self.stop_date = spcal.get()
            self.no_of_person = nop_combo.get()
            self.cabin = class_combo.get().lower()
            self.currency = currency_combo.get().lower()
            window.destroy()

        window = Tk()
        window.title('Cheap flight finder')
        window.config(bg=COLOR, padx=50, pady=50)

        welcome_var = Label(text='Welcome, let me help you find the cheapest flight😊', bg=COLOR, pady=10, font='bold')
        welcome_var.grid(row=0, column=0, columnspan=2)

        name_label = Label(text='Name:', bg=COLOR)
        name_label.grid(row=1, column=0, sticky='w', )
        name_entry = Entry()
        name_entry.grid(row=1, column=1, pady=10)

        from_label = Label(text='From:', bg=COLOR)
        from_label.grid(row=2, column=0, sticky='w',)
        from_entry = Entry()
        from_entry.grid(row=2, column=1, pady=10)

        to_label = Label(text='To:', bg=COLOR)
        to_label.grid(row=3, column=0, sticky='w')
        to_entry = Entry(width=20)
        to_entry.grid(row=3, column=1, pady=10)

        stdate_label = Label(text='Date to start search:', bg=COLOR)
        stdate_label.grid(row=4, column=0, )
        spdate_label = Label(text='Date to stop search :', bg=COLOR)
        spdate_label.grid(row=5, column=0, )

        todays_date = date.today()
        stcal = DateEntry(mindate=todays_date, date_pattern='dd/mm/y')
        stcal.grid(row=4, column=1, pady=10)

        spcal = DateEntry(mindate=todays_date, date_pattern='dd/mm/y')
        spcal.grid(row=5, column=1, pady=10)

        nop_label = Label(text='Number of persons:', bg=COLOR)
        nop_label.grid(row=6, column=0, sticky='w')
        nop_combo = ttk.Combobox(width=27)
        nop_combo['value'] = ('1', '2', '3', '4')
        nop_combo.grid(row=6, column=1, pady=10)
        nop_combo.current(0)

        class_label = Label(text='Cabin class:', bg=COLOR)
        class_label.grid(row=7, column=0, sticky='w')
        class_combo = ttk.Combobox(width=27)
        class_combo['value'] = ('First class', 'Economy premium', 'Business', 'Economy')
        class_combo.grid(row=7, column=1, pady=10)
        class_combo.current(0)

        currency_label = Label(text='Currency:', bg=COLOR)
        currency_label.grid(row=8, column=0, sticky='w')
        currency_combo = ttk.Combobox(width=27)
        currency_combo['value'] = ('Dollar', 'Pounds Sterling', 'Naira', 'Euro')
        currency_combo.grid(row=8, column=1, pady=10)
        currency_combo.current(0)

        button = Button(text='Summit', command=submit)
        button.grid(row=9, column=0, columnspan=2)



        window.mainloop()




