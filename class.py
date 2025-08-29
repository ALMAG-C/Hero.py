class Vehicle:
    def move(self):
        print("Moving...")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈")

# Usage
vehicles = [Car(), Plane()]

for v in vehicles:
    v.move()
