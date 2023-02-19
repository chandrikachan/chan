#to show total vehicle maintanance

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class Bus(Vehicle):
    def fare(self):
        fare_bus = self.capacity * 100 
        total_fare = fare_bus + (0.1 *fare_bus)
        return total_fare
School_bus = Bus("School tata", 85, 10)
print("Total Bus fare is:", School_bus.fare())




