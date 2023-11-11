class Human:
    def __init__(self,name):
        self.name=name
class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passenger = []


    def add_passenger(self,human):
        self.passenger.append(human)
    def print_passengers_names(self):
        if self.passenger != []:
            print(f"names of {self.brand} passenger: ")

            for passenger in self.passenger:
                print(passenger.name)
        else:
            print(f"there are no passenger in {self.brand}")



Nazar = Human("Nazar")
Mary = Human("Mary")

car = Auto("BMV")
car.add_passenger(Nazar)
car.add_passenger(Mary)
car.print_passengers_names()