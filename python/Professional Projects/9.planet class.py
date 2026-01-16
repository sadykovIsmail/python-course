class Planet:
    def __init__(self, name, planet_type, star):
        self.name = name
        self.planet_type = planet_type
        self.star = star
        if not isinstance(self.name, str ) or not isinstance(self.planet_type, str) or not isinstance(self.star, str):
            raise TypeError("name, planet type, and star must be strings")
        if self.name == "" or self.planet_type == "" or self.star == "":
            raise ValueError("name, planet_type, and star must be non-empty strings")
            
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

planet_1 = Planet("d", "d", "dd")
planet_2 = Planet("planet2", "planet_2", "jupiter2")
planet_3 = Planet("planet3", "planet_3", "jupiter3")

print(planet_1)
print(planet_2)
print(planet_3)

print(planet_1.orbit())
print(planet_2.orbit())
print(planet_3.orbit())

print(planet_1.name)