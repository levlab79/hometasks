# Задание 3.
# Запрашиваем у пользователя число n.
n = input('Введите число: ')
# Определяем каждое число суммы.
n_1 = int(n)
n_2 = int(n * 2)
n_3 = int(n * 3)
# Вычисляем сумму.
n_sum = n_1 + n_2 + n_3
# Выводим ответ.
print(f'{n_1} + {n_2} + {n_3} = {n_sum}')
