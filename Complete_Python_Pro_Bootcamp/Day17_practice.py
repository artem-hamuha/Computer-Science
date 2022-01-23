class Car:
    def __init__(self, type: str, year: int, seats: int, side: str):
        """Input type of car, year made, how many seats, and which side the wheel is on."""
        self.type = type
        self.year = year
        self.seats = seats
        self.side = side

    def enter_race_mode(self):
        self.seats = 1
        return f"Seats Reduced to {self.seats}, Race Mode Activated"


my_car = Car("Toyota", 2018, 5, "left")

print(my_car.year)
print(my_car.enter_race_mode())