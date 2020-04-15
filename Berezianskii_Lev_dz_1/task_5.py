# Задание 5.
# Запрашиваем у пользователя значения выручки и издержек фирмы.
revenue = int(input('Введите значение выручки фирмы: '))
expenses = int(input('Введите значение издержек фирмы: '))
# Выручка больше издержек.
if revenue > expenses:
    print('Фирма отработала с прибылью.')
    # Вычисляем рентабельность выручки (соотношение прибыли к выручке).
    profit = (revenue - expenses) / revenue
    print('Рентабельность выручки: {}'.format(round(profit, 3)))
    n_staff = int(input('Введите число сотрудников фирмы: '))
    # Вычисляем прибыль фирмы в расчете на одного сотрудника.
    staff_profit = (revenue - expenses) / n_staff
    print('Прибыль фирмы в расчете на одного сотрудника: {}'.format(round(staff_profit, 3)))
# Издержки больше выручки.
elif revenue < expenses:
    print('Фирма отработала с убытком.')
# Издержки и выручка равны.
else:
    print('Издержки и выручка фирмы равны.')