# Задание 6.
# Определяем допустимые символы.
ALLOWED_CHARS = '1234567890 '


def sum_hours(string_hours):
    '''Складывает часы учебного предмета.'''
    for one_char in string_hours:
        # Убираем все другие символы.
        if not one_char in ALLOWED_CHARS:
            string_hours = string_hours.replace(one_char, '')
    # Переменная для суммы.
    hours_sum = 0
    # Складываем часы.
    for hours in string_hours.split():
        hours_sum += int(hours)
    return hours_sum


# Создаем словарь.
subjects_dict = dict()
# Читаем файл.
with open('task_6_file.txt', 'r', encoding='utf-8') as f:
    for subject in f:
        subject_info = subject.split(':')
        # Заполняем словарь.
        subjects_dict[subject_info[0]] = sum_hours(subject_info[1])

# Выводим словарь.
print(subjects_dict)
