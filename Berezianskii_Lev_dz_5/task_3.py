# Задание 3.

sum_salary = 0
print('Сотрудники с окладом меньше 20 тыс.: ', end='')
with open('task_3_file.txt', 'r', encoding='utf-8') as f:
    for num, person in enumerate(f):
        person_info = person.split()
        sum_salary += int(person_info[1])
        if int(person_info[1]) < 20000:
            print(person_info[0], end=' ')
print(f'\nСредняя величина дохода сотрудников: {sum_salary / (num + 1):.2f}р')