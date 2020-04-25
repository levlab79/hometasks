import sys


def calc_salary(working_hours, salary_per_hour, reward):
    """Функция расчета заработной платы сотрудника"""
    print(f'Заработная плата сотрудника: {int(working_hours) * int(salary_per_hour) + int(reward)}')


# Вызываем функцию, распаковывая параметры запуска.
calc_salary(*sys.argv[1:])
