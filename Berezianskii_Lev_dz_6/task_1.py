# Задание 1.
import time


class TrafficLight():

    def __init__(self):
        self.__color = None
        print('Светофор установлен.')

    def get_info(self):
        if not self.__color is None:
            print(f'Светофор переключен на [{self.__color}] режим на {self.__to} сек.')

    def running(self):
        while True:
            if self.__color is None:
                self.__color = 'красный'
                self.__to = 7

            elif self.__color == 'красный':
                self.__color = 'желтый'
                self.__to = 2

            elif self.__color == 'желтый':
                self.__color = 'зеленый'
                self.__to = 4

            elif self.__color == 'зеленый':
                self.__color = None
                break

            self.get_info()
            time.sleep(self.__to)


# Включаем светофор.
lamp_1 = TrafficLight()
# Начинаем переключать режимы.
lamp_1.running()
