# Задание 5.
import random as rd

# Создаем набор чисел.
rand_numbers = ' '.join([str(rd.randint(-10, 10)) for _ in range(10)])
print(f'Созданный набор чисел: {rand_numbers}')

# Создаем файл и записываем в него набор чисел.
with open('task_5_file.txt', 'w', encoding='utf-8') as f:
    f.write(rand_numbers)

# Переменная для суммы.
numb_sum = 0

# Читаем файл.
with open('task_5_file.txt', 'r', encoding='utf-8') as f:
    # Складываем числа.
    for numb in f.read().split():
        numb_sum += int(numb)

print(f'Сумма чисел: {numb_sum}')
