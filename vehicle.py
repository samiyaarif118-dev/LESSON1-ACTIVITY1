class vehicle:
    def __init__(self, brand, maxspeed):
        self.brand = brand
        self.__maxspeed = maxspeed


    def showdetails(self):
        print("Brand:", self.brand)
        print("Maximum Speed:", self.__maxspeed,"km/h")


class car(vehicle):
    def __init__(self, model,seats, brand, maxspeed):
        self.model = model
        self.seats = seats
        super().__init__(brand, maxspeed)

    def showdetails(self):
        print("Model:", self.model)
        print("Seats:", self.seats)


    def fueltype(self,fuel):
        print("Fuel Type:", fuel)


obj = car("cityrider",5,"BMW",200)
obj.showdetails()
obj.fueltype("petrol")
    
