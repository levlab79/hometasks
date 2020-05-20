# Задание 4, 5 и 6.
class StorageError(Exception):
    pass


class Storage:
    def __init__(self, max_space):
        if max_space and isinstance(max_space, int):
            self._max_space = max_space
            self._storage_list = []
            print(f'Склад создан. Ограничение по вместимости: {max_space}')
        else:
            raise StorageError('Ошибка определения вместимости склада')

    def __str__(self):
        return_list = [f'Свободно: {self._get_free_space()}']
        if self._storage_list:
            return_list.append('Содержимое:')
            for one_equip in self._storage_list:
                return_list.append(f'{one_equip["name"]} {one_equip["firm"]} - {one_equip["quantity"]} шт')
        return '\n'.join(return_list)

    def send_equip(self, equip, quantity):
        '''Отправляет определенное количество техники на склад.'''
        if isinstance(quantity, int):
            # Получаем сколько осталось места.
            free_space = self._get_free_space()
            # Определяем можем ли мы впихнуть еще.
            if quantity <= free_space:
                # Получаем информацию о технике.
                equip_info = equip.info
                # Проверяем есть ли уже такая техника.
                for idx in range(len(self._storage_list)):
                    if equip_info[0] == self._storage_list[idx]["name"] and \
                        equip_info[1] == self._storage_list[idx]["firm"]:
                        # Увеличиваем количество этой техники.
                        self._storage_list[idx]["quantity"] += quantity
                        return
                # Если такой техники еще нет.
                self._storage_list.append({
                    "name": equip_info[0],
                    "firm": equip_info[1],
                    "addition": equip_info[2:],
                    "quantity": quantity
                })
            else:
                raise StorageError('Не хватает свободного места, купите подписку всего за $99/месяц.')
        else:
            raise StorageError('Не удалось распознать количество техники.')

    def _get_free_space(self):
        '''Получаем количество свободного места.'''
        hold_space = 0
        if self._storage_list:
            for one_equip in self._storage_list:
                hold_space += one_equip["quantity"]
        return self._max_space - hold_space


class OfficeEquipments:
    def __init__(self, name, firm):
        self._name = name
        self._firm = firm

    @property
    def info(self):
        return [self._name, self._firm]


class Printer(OfficeEquipments):
    def __init__(self, name, firm, has_colors=False):
        super().__init__(name, firm)
        # Если True -> цветной.
        self._has_colors = has_colors


class Scanner(OfficeEquipments):
    def __init__(self, name, firm, quality):
        super().__init__(name, firm)
        self._quality = quality


class Fax(OfficeEquipments):
    def __init__(self, name, firm, fax_number):
        super().__init__(name, firm)
        self._number = fax_number


# Создаем склад с ограниченной вместимостью - n предметов.
try:
    n = 600
    my_storage = Storage(n)
except StorageError as e:
    print(f'[ошибка] {e}')

# Выводим информацию.
print()
print(my_storage)

# Создаем технику.
printer_1 = Printer('X600', 'Tesla', True)
printer_2 = Printer('RTX3080', 'Nvidia')

scanner_1 = Scanner('XAEA-12', 'SpaceX', 720)
scanner_2 = Scanner('Robo-38', 'Zdorovia', 360)
scanner_3 = Scanner('M177013', 'Zdorovia', 1080)

fax_1 = Fax('XP940', 'Epson', 4827518)
fax_2 = Fax('RGG090', 'Epson', 2957854)

# Отправляем предметы на склад.
my_storage.send_equip(scanner_1, 20)

# Выводим информацию.
print()
print(my_storage)

# Отправляем еще предметы на склад.
my_storage.send_equip(printer_1, 70)
my_storage.send_equip(fax_1, 55)
my_storage.send_equip(fax_2, 150)

# Выводим информацию.
print()
print(my_storage)

# Отправляем технику, которая уже есть на складе.
my_storage.send_equip(printer_1, 245)

# Выводим информацию.
print()
print(my_storage)
print()

try:
    # Пытаемся добавить больше, чем склад может вместить.
    my_storage.send_equip(printer_2, 80)
except StorageError as e:
    print(f'[ошибка] {e}')

# Выводим информацию.
print()
print(my_storage)
