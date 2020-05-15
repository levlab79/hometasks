# Задание 4.

class Car():

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.now_speed = 0
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        self.now_speed = self.speed
        print(f'Машина {self.name} поехала со скоростью {self.now_speed} км/ч.')

    def show_speed(self):
        if self.now_speed:
            print(f'Машина {self.name} едет со скоростью {self.now_speed} км/ч.')
        else:
            print(f'Машина {self.name} стоит на месте.')

    def stop(self):
        self.now_speed = 0
        print(f'Машина {self.name} остановилась.')

    def turn(self, direction):
        if self.now_speed:
            print(f'Машина {self.name} развернулась в направлении: {direction}.')
        else:
            print(f'Машина {self.name} не может развернуться, когда стоит на месте.')


class TownCar(Car):

    def show_speed(self):
        if self.now_speed:
            print(f'Машина {self.name} едет со скоростью {self.now_speed} км/ч.')
            if self.now_speed > 60:
                print('Превышение скорости!')
        else:
            print(f'Машина {self.name} стоит на месте.')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.now_speed:
            print(f'Машина {self.name} едет со скоростью {self.now_speed} км/ч.')
            if self.now_speed > 40:
                print('Превышение скорости!')
        else:
            print(f'Машина {self.name} стоит на месте.')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)
        self._is_police = True


# Создадим полицейский автомобиль.
police_car = PoliceCar(70, 'green', 'Lexus')
# Поедем на ней.
police_car.go()
# По городу.
police_car.turn('Город')
# Остановимся.
police_car.stop()
# Попробуем развернуться.
police_car.turn('Пляж')
police_car.go()
police_car.turn('Пляж')
print()

# Создадим городскую машину.
town_car = TownCar(70, 'red', 'LADA')
town_car.turn('Склад')
town_car.go()
town_car.turn('Склад')
# Посмотрим на скорость.
town_car.show_speed()
print()

# Создадим спортивную машину.
town_car = SportCar(240, 'white', 'Tesla')
town_car.go()
# Посмотрим на скорость.
town_car.show_speed()
town_car.turn('Пляж')
print()

police_car.turn('Tesla')
