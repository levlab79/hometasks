def my_func(number, rate):
    """Функция возвращает число, возведенное в отрицательную степень."""
    result_number = 1
    # Производим возведение в положительную степень.
    for el in range(rate * (-1)):
        result_number *= number
    # Переворачиваем дробь, т.к. степень отрицательная.
    result_number = 1 / result_number
    # Возвращаем результат.
    return result_number


def my_func_easy(number, rate):
    """Функцию возвращает число, возведенное в степень."""
    return number ** rate


user_number = float(input('Введите число: '))
user_rate = int(input('Введите степень: '))
# Вызываем функцию.
print(f'Результат (без использования **): {my_func(user_number, user_rate)}')
print(f'Результат (с использованием **): {my_func_easy(user_number, user_rate)}')
