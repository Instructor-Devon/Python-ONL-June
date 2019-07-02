from driver import Driver
class Car:
    # attributes (things the class posesses)
        # make, model, year

    # constructor
            # Car ("Ferrari", "Testatrosa")
    def __init__(self, make, model, year, driver):
        # string
        self.make = make
        # string
        self.model = model
        # int
        self.year = year
        # Driver
        self.driver = driver
        # int
        self.odometer = 0
    
    # methods (actions the class can perform)
        # honk, drive

    def honk(self):
        print("HONK HONK!")

    def drive(self, distance):
        print(f"{self.driver.name} shouts {self.driver.motto} as they drive the {self.make}")
        self.odometer += distance

    def __repr__(self):
        return f"Car: {self.make}, {self.model}"
    

