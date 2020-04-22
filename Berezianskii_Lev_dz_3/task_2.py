def print_user_info(name, surname, b_date, city, email, phone):
    print(f'{surname} {name} родился {b_date}, проживает в городе {city}. Контакты: {email}, {phone}')


# Вызываем функцию с именованными аргументами.
print_user_info(name='Максим', surname='Волков', b_date='10.05.1997', city='Калининград',
                email='max_volkov@gmail.com', phone='89114637094')
