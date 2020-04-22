def int_func(word):
    """Функция, возвращающая то же слово, но с заглавной буквы."""
    # Получаем заглавную версию первой буквы слова (с помощью сдвига в таблице Unicode).
    big_letter = chr(ord(word[0]) - 32)
    # Возвращаем строку из заглавной буквы и оставшегося слова.
    return big_letter + word[1:]


user_string = input('Введите строку из слов: ')
# Создаем список из слов, записанных через пробел.
user_list = user_string.split()
new_string = list()
# Обрабатываем каждое слово.
for one_word in user_list:
    new_string.append(int_func(one_word))
# Выводим получившуюся строку.
print(' '.join(new_string))
