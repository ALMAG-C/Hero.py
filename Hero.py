class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Origin: {self.origin}")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")


# Inheritance Example: a subclass
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, origin, flying_speed):
        super().__init__(name, power, origin)
        self.flying_speed = flying_speed

    def use_power(self):
        print(f"{self.name} flies at {self.flying_speed} km/h using {self.power}!")

# Usage
hero = Superhero("Flash", "Super Speed", "Metahuman")
hero.display_info()
hero.use_power()

fly_hero = FlyingSuperhero("Superman", "Flight", "Krypton", 2000)
fly_hero.display_info()
fly_hero.use_power()