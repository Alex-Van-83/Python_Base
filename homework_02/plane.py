"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight, fuel, fuel_consumption, max_cargo, cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        new_cargo = self.cargo + cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += new_cargo

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0
        return cargo
