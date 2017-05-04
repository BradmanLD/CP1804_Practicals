from taxi import Taxi

# Test creating a new taxi
prius_one = Taxi("Prius 1", 100)

# Test driving & __str__
prius_one.drive(40)
print(prius_one)

# Test resetting current fare
prius_one.start_fare()
prius_one.drive(100)
print(prius_one)
