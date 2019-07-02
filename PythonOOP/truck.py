from car import Car
class IceCreamTruck(Car):

    def __init__(self, make, model, year, driver):
        super().__init__(make, model, year, driver)

    def playSong(self):
        print("do doo doo do doo")

    def __repr__(self):
        return f"Ice Cream Truck: {self.make}, {self.model}"