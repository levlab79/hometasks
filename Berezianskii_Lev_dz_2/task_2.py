# Задание 2.

# Создаем список.
user_list = list()
# Входим в цикл заполнения списка.
while True:
    new_element = input('Введите новый элемент списка (чтобы закончить, оставьте поле пустым): ')
    # Проверяем является ли новый элемент строкой "stop"
    if new_element:
        # Добавляем новый элемент в список.
        user_list.append(new_element)
    else:
        # Выходим из цикла.
        break

# Создал готовые списоки (с нечетным и четным количеством элементов) для удобства проверки.
# user_list = ['first', False, 4123, 'second', True, 0.12, 'Megumin']
# user_list = ['first', False, 4123, 'second', True, 0.12]

print(f'Исходный список: {user_list}')

# Я не был уверен можно ли так поступить.
# Но все-таки решил использовать range(), т.к. в методичке по уроку №2 он используется в примерах.
# И-так используем цикл for in по последовательности range() от 1 по len()
# с шагом 2
for index in range(1, len(user_list), 2):
    # Меняем элементы местами.
    user_list[index - 1], user_list[index] = user_list[index], user_list[index - 1]

print(f'Обработанный список: {user_list}')
