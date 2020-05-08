# Задание 2.

with open('task_2_file.txt', 'r', encoding='utf-8') as f:
    for num, line in enumerate(f):
        print(f'В строке №{num + 1} слов: {len(line.split())}')
print(f'Количество строк: {num + 1}')
