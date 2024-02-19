import math


class Koonus:
    def __init__(self):
        self.radius = 0
        self.height = 0

    def set_values(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_values(self):
        # Arvutame koonuse ruumala ja pindala
        volume = (1 / 3) * math.pi * self.radius ** 2 * self.height
        surface_area = math.pi * self.radius ** 2
        hypotenuse = math.sqrt(self.radius ** 2 + self.height ** 2)
        return volume, surface_area, hypotenuse
