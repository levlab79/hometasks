# Задание 2.

class MyZeroDivisionError(Exception):
    pass

while True:
    user_input = input('Введите числа a и b через пробел (пусто -> выход): ')
    if user_input:
        try:
            user_numbs = user_input.split()
            a = int(user_numbs[0])
            b = int(user_numbs[1])
            if not b:
                raise MyZeroDivisionError("Деление на нуль")
            c = a / b
        except MyZeroDivisionError:
            print(f'{a} / {b} = 0')
        except Exception as e:
            print(f'[Ошибка] {e}')
        else:
            print(f'{a} / {b} = {c}')
    else:
        break
