# Задание 7.

class ComplexNumber:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        '''Вывод на экран'''
        return_list = []
        if self._a != 0:
            return_list.append(str(self._a))
            if self._b > 0:
                return_list.append('+')
        if self._b != 0:
            return_list.append(str(self._b))
            return_list.append('i')
        if return_list:
            return ''.join(return_list)
        return '0'
    
    def __add__(self, other):
        '''Сложение'''
        return ComplexNumber(self._a + other._a, self._b + other._b)
    
    def __mul__(self, other):
        '''Умножение'''
        return ComplexNumber(self._a * other._a - self._b * other._b, \
            self._b * other._a + self._a * other._b)


numb_1 = ComplexNumber(5, 3)
numb_2 = ComplexNumber(4, -2)
numb_3 = ComplexNumber(0, 7)
numb_4 = ComplexNumber(0, -3)
numb_5 = ComplexNumber(-2, 0)
numb_6 = ComplexNumber(0, 0)

print('Создаем комплексные числа:')
print(numb_1)
print(numb_2)
print(numb_3)
print(numb_4)
print(numb_5)
print(numb_6)

print('\nПроверяем сложение:')
print(f'({numb_1}) + ({numb_2}) = {numb_1 + numb_2}')
print(f'({numb_1}) + ({numb_3}) = {numb_1 + numb_3}')
print(f'({numb_2}) + ({numb_5}) = {numb_2 + numb_5}')
print(f'({numb_4}) + ({numb_6}) = {numb_4 + numb_6}')

print('\nПроверяем умножение:')
print(f'({numb_1}) * ({numb_2}) = {numb_1 * numb_2}')
print(f'({numb_1}) * ({numb_3}) = {numb_1 * numb_3}')
print(f'({numb_2}) * ({numb_5}) = {numb_2 * numb_5}')
print(f'({numb_4}) * ({numb_6}) = {numb_4 * numb_6}')
