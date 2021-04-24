class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
passengers = ["Jonh", "Mike", "Oven", "Nary"]

for name in passengers:
    if flight.add_passenger(name):
        print(f"Add {name} to flight successfully")
    else:
        print(f"No seat available for {name}")