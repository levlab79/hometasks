def my_func(number, rate):
    """Функция возвращает число, возведенное в степень."""
    # Меняем знак степени если она отрицательная.
    new_rate = rate * (-1) if rate < 0 else rate
    result_number = 1
    # Производим возведение в положительную степень.
    for el in range(new_rate):
        result_number *= number
    # Переворачиваем стол, если степень отрицательная.
    result_number = 1 / result_number if rate < 0 else result_number
    # Возвращаем результат.
    return result_number


def my_func_easy(number, rate):
    """Функцию возвращает число, возведенное в степень."""
    return number ** rate


user_number = int(input('Введите число: '))
user_rate = int(input('Введите степень: '))
# Вызываем функцию.s
print(f'Результат (без использования **): {my_func(user_number, user_rate)}')
print(f'Результат (с использованием **): {my_func_easy(user_number, user_rate)}')
