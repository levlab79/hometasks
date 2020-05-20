# Задание 3.

class ElDigitError(Exception):
    pass


def check_el(el):
    try:
        float(el)
    except:
        raise ElDigitError('Это не число!')


print('Для выхода введите "stop" или оставьте строку пустой.')
user_list = []
while True:
    user_input = input('Введите число: ')
    # Проверяем, что ввел пользователь.
    if user_input and user_input != 'stop':
        try:
            check_el(user_input)
        except ElDigitError as e:
            print(f'[ОШИБКА] {e}')
        else:
            user_list.append(user_input)
    else:
        break

if user_list:
    print(f'Список: {user_list}')
else:
    print('Список пустой!')
