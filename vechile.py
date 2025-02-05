from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    def drive(self, distance: float):
        required_fuel = distance * (self.fuel_consumption + 0.9)  # Air conditioner consumption
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def drive(self, distance: float):
        required_fuel = distance * (self.fuel_consumption + 1.6)  # Air conditioner consumption
        if self.fuel_quantity >= required_fuel:
            self.fuel_quantity -= required_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel * 0.95  # Truck keeps only 95% of refueled fuel


# Test Cases
car = Car(20, 5)  # 20 liters of fuel, 5 liters/km consumption
car.drive(3)  # Drive 3 km

print(car.fuel_quantity)  # Expected: 2.299999999999997

car.refuel(10)  # Refuel 10 liters
print(car.fuel_quantity)  # Expected: 12.299999999999997
