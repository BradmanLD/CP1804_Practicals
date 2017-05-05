from prac08.car import Car
from random import randint


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0.0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if self.reliability > randint(0, 100):
            distance_driven = super().drive(distance)
            return distance_driven
        return 0