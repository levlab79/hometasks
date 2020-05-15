# Задание 2.

class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_asphalt_mass(self, asphalt_mass_per_sm, depth):
        self.result_mass = self._length * self._width * asphalt_mass_per_sm * depth / 1000
        print(f'{self._length} м * {self._width} м * {asphalt_mass_per_sm} кг * {depth} см = {self.result_mass:.2f} т')


road_1 = Road(length=5000, width=20)
road_1.calc_asphalt_mass(asphalt_mass_per_sm=25, depth=5)

road_2 = Road(length=15000, width=35)
road_2.calc_asphalt_mass(asphalt_mass_per_sm=25, depth=4)
