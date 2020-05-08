# Задание 7.
import json

# Создаем словарь для фирм.
firms_dict = dict()
# Сумма прибыли.
sum_profit = 0
# Кол-во фирм с прибылью
numb_profit = 0
# Читаем файл построчно.
with open('task_7_file.txt', 'r', encoding='utf-8') as f:
    for firm in f:
        firm_info = firm.split()
        # В задании написано, что фирмы с убытками также включать в словарь.
        # Поэтому я решил оставить им знак *минус*, чтобы были видны убытки.
        firm_result = int(firm_info[2]) - int(firm_info[3])
        # Если фирма отработала с прибылью.
        if firm_result > 0:
            sum_profit += firm_result
            numb_profit += 1
        firms_dict[firm_info[0]] = firm_result

# Определяем среднюю прибыль.
average_profit_dict = {"average_profit": sum_profit / numb_profit}

# Создаем общий список.
firms_list = [firms_dict, average_profit_dict]

# Сохраняем в соответствующий файл.
with open('task_7_file.json', 'w', encoding='ascii') as f:
    json.dump(firms_list, f)
