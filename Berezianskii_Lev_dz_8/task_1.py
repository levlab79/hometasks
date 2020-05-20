# Задание 1.

class UserDateError(Exception):
    pass


class Date:
    def __init__(self, string_date):
        self._date = None
        try:
            self._date = Date._convert_to_int(string_date)
        except UserDateError as e:
            print(f'[Ошибка даты] {e}')
        except Exception as e:
            print(f'[Другая ошибка] {e}')

    def __str__(self):
        return f'Дата: {self._date}'

    @classmethod
    def _convert_to_int(cls, string_date):
        '''Преобразуем дату в int.'''
        date_list = string_date.split('-')
        if len(date_list) == 3:
            return cls._check_valid(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        raise UserDateError('Ошибка формата даты!')

    @staticmethod
    def _check_valid(*tuple_date):
        '''Проверяем дату на правильность.'''
        if 1 <= tuple_date[0] <= 31 and 1 <= tuple_date[1] <= 12 and 0 < tuple_date[2]:
            return tuple_date
        raise UserDateError('Некорректная дата!')


user_date_1 = Date('13-9-2016')
user_date_2 = Date('04-11-2000')
print(user_date_1)
print(user_date_2)
