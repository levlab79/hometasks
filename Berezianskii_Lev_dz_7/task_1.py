# Задание 1.


class Matrix:

    def __init__(self, matrix_list):
        self._main_list = matrix_list

    def __add__(self, other):
        # Делаем проверку на одинаковость размеров матриц.
        if self._check_matrix(other):
            # Создаем новую матрицу.
            new_matrix = []
            for idx in range(len(self._main_list)):
                small_list = []
                for deep_idx in range(len(self._main_list[idx])):
                    small_list.append(self._main_list[idx][
                                      deep_idx] + other._main_list[idx][deep_idx])
                new_matrix.append(small_list)
            return Matrix(new_matrix)
        else:
            raise ValueError("Размеры матриц не совпадают!")

    def __str__(self):
        print_list = []
        for one_string in self._main_list:
            for one_numb in one_string:
                print_list.append(f'{one_numb:^5}')
            print_list.append('\n')
        return ''.join(print_list)

    def _check_matrix(self, other):
        '''Проверяет матрицы на совпадение по размерам.'''
        result = True
        if len(self._main_list) == len(other._main_list):
            for idx in range(len(self._main_list)):
                if len(self._main_list[idx]) != len(other._main_list[idx]):
                    result = False
        else:
            result = False
        return result


matrix_1 = Matrix([
    [5, 1, -5],
    [0, 23, 9],
    [5, -2, 6]
])

matrix_2 = Matrix([
    [7, 4, -5],
    [0, -14, 7],
    [14, -2, 9]
])

print('Первая матрица (A):')
print(matrix_1)
print('Вторая матрица (B):')
print(matrix_2)

matrix_result_1 = matrix_1 + matrix_2
print('Результат их сложения (A + B):')
print(matrix_result_1)

matrix_3 = Matrix([
    [5, 13, -4],
    [0, -2, 7],
    [0, 5, 29]
])

print('Третья матрица (C):')
print(matrix_3)

print('Результат сложения трёх матриц (A + B + C):')
matrix_result_2 = matrix_1 + matrix_2 + matrix_3
print(matrix_result_2)

matrix_4 = Matrix([
    [7, 4, -5],
    [0, -14, 7]
])

matrix_5 = Matrix([
    [0, 23, 9],
    [5, -2, 6]
])

print('Четвертая и пятые матрицы (D и E):')
print(f'{matrix_4}\n{matrix_5}')

print('Результат сложения (D + E):')
print(matrix_4 + matrix_5)

matrix_6 = Matrix([
    [7, 4],
    [0, -14],
    [14, -2]
])

matrix_7 = Matrix([
    [5, 1, ],
    [0, 23],
    [5, -2]
])

print('Шестая и седьмая матрицы (F и G):')
print(matrix_6)
print(matrix_7)

print('Результат сложения (F + G):')
print(matrix_6 + matrix_7)
