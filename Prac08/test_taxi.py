from prac08.taxi import Taxi, SilverServiceTaxi

# Test creating a new taxi
prius_one = Taxi("Prius 1", 100)

# Test driving & __str__
prius_one.drive(40)
print(prius_one)

# Test resetting current fare
prius_one.start_fare()
prius_one.drive(100)
print(prius_one)

# Test Silver Service
silver_surfer = SilverServiceTaxi("Silver Surfer", 100, 4.85)
print(silver_surfer.price_per_km)
print(silver_surfer)

# Test with expected outputs
hummer = SilverServiceTaxi("Hummer", 200, 2)
hummer.drive(10)
print(hummer.get_fare())  # Expected $28.50 - Got $28.50

