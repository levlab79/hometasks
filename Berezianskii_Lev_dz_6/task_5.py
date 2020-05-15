# Задание 5.

class Stationery():

    def __init__(self, title):
        self.title = title
        print(f'Куплена канцелярская принадлежность: {self.title}')

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def __init__(self, title='Ручка'):
        super().__init__(title)
        self.title = title

    def draw(self):
        print('Начинаю писать текст.')


class Pencil(Stationery):

    def __init__(self, title='Карандаш'):
        super().__init__(title)
        self.title = title

    def draw(self):
        print('Начинаю чертить.')


class Handle(Stationery):

    def __init__(self, title='Маркер'):
        super().__init__(title)
        self.title = title

    def draw(self):
        print('Начинаю выделять текст.')


# Покупаем ручку.
pen_1 = Pen()
# Начинаем писать текст.
pen_1.draw()

print()

pencil_1 = Pencil()
pencil_1.draw()

print()

handle_1 = Handle()
handle_1.draw()

print()

pen_2 = Stationery('Автоматическая ручка.')
pen_2.draw()
