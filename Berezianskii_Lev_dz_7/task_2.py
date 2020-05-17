# Задание 2.
from abc import ABC, abstractmethod


class Cloths(ABC):
    fabric_count = 0

    def __init__(self, title):
        self._title = title

    @abstractmethod
    def calc_intake(self):
        pass

    def _update_fabric_count(self, cloths_count):
        Cloths.fabric_count += cloths_count


class Coat(Cloths):

    def __init__(self, title, size):
        super().__init__(title)
        self._size = size

    @property
    def calc_intake(self):
        cloths_count = self._size / 6.5 + 0.5
        super()._update_fabric_count(cloths_count)
        return cloths_count


class Suit(Cloths):

    def __init__(self, title, height):
        super().__init__(title)
        self._height = height

    @property
    def calc_intake(self):
        cloths_count = 2 * self._height + 0.3
        super()._update_fabric_count(cloths_count)
        return cloths_count

# Создаем пальто.
coat_1 = Coat('Пальто черное', 56)
print(f'Ушло ткани: {coat_1.calc_intake:.2f}')
print(f'Общий расход ткани: {Cloths.fabric_count:.2f}')

print()
coat_2 = Coat('Пальто короткое', 48)
print(f'Ушло ткани: {coat_2.calc_intake:.2f}')
coat_3 = Coat('Пальто серое', 60)
print(f'Ушло ткани: {coat_3.calc_intake:.2f}')
print(f'Общий расход ткани: {Cloths.fabric_count:.2f}')

print()
suit_1 = Suit('Костюм роскошный', 182)
print(f'Ушло ткани: {suit_1.calc_intake:.2f}')
suit_2 = Suit('Костюм черный', 176)
print(f'Ушло ткани: {suit_2.calc_intake:.2f}')
print(f'Общий расход ткани: {Cloths.fabric_count:.2f}')
