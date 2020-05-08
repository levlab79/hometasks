# Задание 1.

with open('task_1_file.txt', 'w', encoding='utf-8') as f:
    while True:
        new_string = input('Новая строка: ')
        if new_string:
            f.write(f'{new_string}\n')
        else:
            break
