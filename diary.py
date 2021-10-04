entries = []

class DiaryEntry(object):

    def __init__(self):
        self.message = ''
        self.day = 0
        self.month = 0
        self.year = 0

        self.event_type = ''
        self.names = []

    def set_message(self, m):
        self.message = m

    def get_message(self):
        return self.message

    def set_day(self, d):
        self.day = d

    def get_day(self):
        return self.day

    def set_month(self, m):
        self.month = m

    def get_month(self):
        return self.month

    def set_year(self, y):
        self.year = y

    def get_year(self):
        return self.year
    
    def set_event_type(self, e):
        self.event_type = e

    def get_event_type(self):
        return self.event_type

    def set_names(self, n):
        self.names = n

    def get_names(self):
        return self.names

    def display(self):
        print(f'{self.day}-{self.month}-{self.year}: {self.message}')
        if self.event_type == 'group':
            print(f'\tNames: {self.names}')


def add_entry(message, day, month, year, event_type, names):
    global entries
    # Create a DiaryEntry object
    d = DiaryEntry()
    d.set_message(message)
    d.set_day(day)
    d.set_month(month)
    d.set_year(year)
    d.set_event_type(event_type)
    d.set_names(names)

    # Add it to the entries list
    entries.append(d)

    return entries

def display_all_entries():
    global entries
    for i in range(len(entries)):
        entries[i].display()

def display_todays_entries(day, month, year):
    global entries
    for i in range(len(entries)):
        # Check if the values for day, month, year inside the object match
        if entries[i].get_day() == day and entries[i].get_month() == month and entries[i].get_year() == year:
            entries[i].display()

def display_months_entries(month, year):
    global entries
    for i in range(len(entries)):
        # Check if the values for month, year inside the object match
        if entries[i].get_month() == month and entries[i].get_year() == year:
            entries[i].display()
