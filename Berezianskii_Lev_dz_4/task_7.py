from itertools import count


def get_factorial():
    # Начинаем цикл.
    for n_factorial in count():
        result_number = 1
        # Вычисляем факториал текущего числа.
        for number in range(2, n_factorial + 1):
            result_number *= number
        # Возвращаем число и его факториал.
        yield n_factorial, result_number


def get_fibonacci():
    # Переменные двух предыдущий чисел.
    pre_previous = 1
    previous = 1
    # Начинаем цикл с 3, т.к. 1е и 2е числа уже заданы.
    for n_fibonacci in count(3):
        # Вычисляем текущее число Фибоначчи.
        result_fibonacci = pre_previous + previous
        # Изменяем предыдущие два числа.
        pre_previous, previous = previous, result_fibonacci
        # Возвращаем номер этого числа и самое текущее число.
        yield n_fibonacci, result_fibonacci


# Количество факториалов и чисел Фибоначчи, которые будут вычислены.
last_number = 20

# Выводим факториалы.
print('Факториалы: ')
for el in get_factorial():
    if el[0] > last_number:
        break
    else:
        print(f'{el[0]}! = {el[1]}')

print('\n' + '=' * 30 + '\n' * 2 + 'Числа Фибоначии:')

# Выводим числа Фибоначчи.l
for el in get_fibonacci():
    if el[0] > last_number:
        break
    else:
        print(el[1], end=' ')
