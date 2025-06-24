class Car:
    brand = ""
    name = ""
    speed = 0

    def __init__(self, brand, name, speed):
        self.brand = brand
        self.name = name
        self.speed = speed

    def run(self):
        print(f"The car is running at {self.speed} km/h")

class Truck(Car):
    capacity = ""

    def __init__(self, capacity):
        super().__init__("Man", "idk", 100)
        self.capacity = capacity

    def run(self):
        print("Truck ran")

car1 = Car("Mercedes", "cls", 200)
car2 = Car("lamborghini", "revuelto", 300)

print(car1.brand)
print(car2.brand)
car1.run()

truck1 = Truck("Big")
print(truck1.capacity)
truck1.run()