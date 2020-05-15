# Задание 3.

class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
        print(f'Создана запись: {self.name} - {self.position}')


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход сотрудника {self.name}: {self._income["wage"] + self._income["bonus"]}')


# Создаем записи.
worker_1 = Position('Борис', 'Сорокин', 'Старший менеджер', 45000, 12500)
worker_2 = Position('Андрей', 'Котов', 'Генеральный директор', 56000, 20000)
print()
# Получаем полное имя.
worker_1.get_full_name()
# Получаем доход с учетом премии.
worker_1.get_total_income()
print()
# Получаем полное имя.
worker_2.get_full_name()
# Получаем доход с учетом премии.
worker_2.get_total_income()
