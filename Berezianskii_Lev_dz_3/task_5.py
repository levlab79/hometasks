def sum_numbers(number_list):
    number_sum = 0
    for number in number_list:
        # Не сказано, что числа целые.
        number_sum += float(number)
    # Возвращаем получившуюся сумму.
    return number_sum


# Определяем переменную суммы.
user_sum = 0
# Входим в цикл.
while True:
    user_string = input('Введите числа (для выхода - "n"): ')
    # Если введен только специальный символ
    if user_string == "n":
        # Выходим из цикла.
        break
    else:
        # Заменяем специальный символ, если он существует.
        new_user_string = user_string.replace('n', '')
        # Вызываем функцию и увеличиваем общую сумму.
        user_sum += sum_numbers(new_user_string.split())
        print(f'Сумма всех чисел: {user_sum}')
        # Если в строке с числами был введен спецсимвол.
        if "n" in user_string:
            # Выходим из цикла.
            break
