# Задание 4.

# Получаем строку пользователя.
# user_string = input('Введите строку: ')
user_string = 'Анизотропия представляет собой различие свойств среды'

# Разбиваем строку.
words_list = user_string.split()
# Выводим пронумерованные слова.
for index, word in enumerate(words_list):
    print(f'№{index + 1} - {word[:10]}')
