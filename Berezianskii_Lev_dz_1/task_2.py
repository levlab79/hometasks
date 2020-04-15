# Задание 2.
# Запрашиваем время в секундах, сразу преобразуем в число.
# user_sec = int(input('Введите время в секундах: '))
user_sec = int('5102')

# Определяем количество часов.
hours = user_sec // 3600
# Определяем количество минут.
minutes = (user_sec - hours * 3600) // 60
# Определяем количество секунд.
seconds = user_sec - hours * 3600 - minutes * 60

# Eсли количество часов меньше 10, добавляем 0 в начале для правильного
# отображения.
if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'

# Выводим результат.
print(f'{hours}:{minutes}:{seconds}')
