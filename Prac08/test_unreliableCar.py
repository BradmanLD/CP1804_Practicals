from prac08.unreliableCar import UnreliableCar

# Test creating unreliable car
terrible_car = UnreliableCar("Terrible", 100, 0)
# print(terrible_car)

# Test reliability with no chance of success
print("0% Chance Test")
terrible_car.drive(50)
print(terrible_car)

# Test reliability with 100% chance of success
print("100% Chance Test")
terrible_car.reliability = 100
terrible_car.drive(50)
print(terrible_car)

# Test reliability with 50% chance of success
terrible_car.reliability = 50
print("Start of 50% Test")
while terrible_car.fuel != 0:
    terrible_car.drive(25)
    print(terrible_car)
