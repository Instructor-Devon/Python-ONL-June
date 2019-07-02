from car import Car
from truck import IceCreamTruck
from driver import Driver

lars = Driver()

ferrari = Car("Ferrari", "Testarosa", 1989, lars)

# print(type(ferrari)) # Car
# print(type("Hello World"))
# print(type(lars))
# ferrari.honk()
# ferrari.drive(60)

# volvo = Car("Volvo", "240 Sedan", 1987, lars)
# volvo.honk()
# volvo.drive(30)

d = Driver()

ice = IceCreamTruck("Jeep", "Cheroke", 1995, d)

print(type(ice))