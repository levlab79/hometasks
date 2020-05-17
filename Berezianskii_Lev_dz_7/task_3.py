# Задание 3.


class Cell:
    def __init__(self, count):
        if count > 0:
            self._count = count
        else:
            raise ValueError('Количество ячеек клетки должно быть положительно.')

    def __add__(self, other):
        '''Сложение'''
        if self._check_class(other):
            return Cell(self._count + other._count)

    def __sub__(self, other):
        '''Вычитание'''
        if self._check_class(other):
            result_cell = self._count - other._count
            if result_cell > 0:
                return Cell(result_cell)
            else:
                raise ValueError('Результат вычитания клеток должен быть больше нуля.')

    def __mul__(self, other):
        '''Умножение'''
        if self._check_class(other):
            return Cell(self._count * other._count)

    def __truediv__(self, other):
        '''Обычное деление'''
        if self._check_class(other):
            return Cell(self._count // other._count)

    def _check_class(self, other_cl):
        '''Проверяет является данные класс классом клетки'''
        if isinstance(other_cl, Cell):
            return True
        else:
            raise TypeError(f'{type(other_cl)} не является классом клетки.')

    def __str__(self):
        '''Выводим клетки на экран'''
        # Определяем оптимальное количество столбцов, что фигура -> к квадрату.
        float_columns = self._count ** 0.5
        columns = int(float_columns) + 1 if float_columns % 1 else int(float_columns)
        return self._make_order(columns)

    def _make_order(self, columns):
        '''Организуем структуру клетки'''
        return_list = []
        for numb in range(self._count):
            return_list.append('*')
            if not (numb + 1) % columns:
                return_list.append('\n')
        return ''.join(return_list)

    @property
    def cell_count(self):
        return self._count


# Создаем клетки.
cell_1 = Cell(74)
cell_2 = Cell(25)
cell_3 = Cell(13)

print(f'Клетки 1 = {cell_1.cell_count}; 2 = {cell_2.cell_count} и 3 = {cell_3.cell_count}:\n')
print(cell_1)
print()
print(cell_2)
print()
print(cell_3)

# Складываем клетки.
cell_4 = cell_1 + cell_2
cell_5 = cell_1 + cell_3 + cell_4

print(f'\nКлетки 4 и 5 (K4 = K1 + K2 = {cell_4.cell_count}; K5 = K1 + K3 + K4 = {cell_5.cell_count}):\n')
print(cell_4)
print()
print(cell_5)

# Вычитаем клетки.
# cell_6 = cell_4 - cell_5 # <- прилетит бан
cell_7 = cell_5 - cell_4
cell_8 = cell_1 - cell_2 - cell_3

print(f'\nКлетки 7 и 8 (К7 = К5 - К4 = {cell_7.cell_count}; К8 = К1 - К2 - К3 = {cell_8.cell_count}):\n')
print(cell_7)
print()
print(cell_8)

# Умножаем клетки.
cell_9 = cell_3 * cell_8
cell_10 = cell_2 * cell_3 * cell_8

print(f'\nКлетки 9 и 10 (К9 = К3 * К8 = {cell_9.cell_count}; К10 = К2 * К3 * К8 = {cell_10.cell_count}):\n')
print(cell_9)
print()
print(cell_10)

# Деление клеток.
cell_11 = cell_9 / cell_2
cell_12 = cell_10 / cell_1 / cell_2

print(f'\nКлетки 11 и 12 (К11 = К9 / К2 = {cell_11.cell_count}; К12 = К10 / К1 / К2 = {cell_12.cell_count}):\n')
print(cell_11)
print()
print(cell_12)
