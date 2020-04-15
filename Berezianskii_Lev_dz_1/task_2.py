# Задание 2.
# запрашиваем время в секундах, сразу преобразуем в число
user_sec = int(input('Введите время в секундах: '))

# определяем количество часов
hours = user_sec // 3600
# определяем количество минут
minutes = (user_sec - hours * 3600) // 60
# определяем количество секунд
seconds = user_sec - hours * 3600 - minutes * 60

# если количество часов меньше 10, добавляем нуль в начале для приятного отображения
if hours < 10:
    hours = f'0{hours}'
if minutes < 10:
    minutes = f'0{minutes}'
if seconds < 10:
    seconds = f'0{seconds}'

# выводим результат
print(f'{hours}:{minutes}:{seconds}')