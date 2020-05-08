# Задание 4.
# Словарь для замены числительных.
translate_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять",
    "Six": "Шесть",
    "Seven": "Семь",
    "Eight": "Восемь",
    "Nine": "Девять",
    "Ten": "Десять"
}

# Формируем список новых строк.
new_string_list = []

# Открываем файл на чтение.
with open('task_4_file.txt', 'r', encoding='utf-8') as f:
    # Считываем данные построчно.
    for line in f:
        # Получаем английское числительное.
        eng_number = line.split(' — ')[0]
        # Редактируем строку и добавляем в список новых строк.
        new_string_list.append(line.replace(eng_number, translate_dict[eng_number]))

# Записываем список новых строк в новый текстовый файл.
with open ('task_4_file_new.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_string_list)

