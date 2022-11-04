from abc import ABC
from homework_02.exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):

    def __init__(self, weight=0, fuel=0, fuel_consumption=10, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        need_fuel = self.fuel_consumption * distance
        if need_fuel <= self.fuel:
            self.fuel -= need_fuel
        else:
            raise NotEnoughFuel
