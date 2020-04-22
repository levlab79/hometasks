def numbers_division(number_1, number_2):
    """Выполняем деление двух чисел."""
    if number_2:
        return number_1 / number_2
    else:
        return -1


user_number_1 = float(input('Введите первое число: '))
user_number_2 = float(input('Введите второе число: '))
# Вызываем функцию с позиционными аргументами.
number_result = numbers_division(user_number_1, user_number_2)
# Выводим информацию.
print(f'{user_number_1} / {user_number_2} = {number_result if not number_result == -1 else "деление на нуль"}\n')
