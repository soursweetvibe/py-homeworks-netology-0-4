"""
Задание 1.
Итератор FlatIterator для плоского представления списка списков.
"""


class FlatIterator:
    """
    Итератор для преобразования списка списков в плоскую последовательность.
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.outer_cursor = 0
        self.inner_cursor = 0
        return self

    def __next__(self):
        # Проходим по внешним спискам
        while self.outer_cursor < len(self.list_of_list):
            # Проверяем, есть ли еще элементы во внутреннем списке
            if self.inner_cursor < len(self.list_of_list[self.outer_cursor]):
                item = self.list_of_list[self.outer_cursor][self.inner_cursor]
                self.inner_cursor += 1
                return item
            else:
                # Переходим к следующему внешнему списку
                self.outer_cursor += 1
                self.inner_cursor = 0
        
        # Если дошли до конца, выбрасываем StopIteration
        raise StopIteration


def test_1():
    """
    Тестовая функция для проверки работы FlatIterator.
    """
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    
    print("Тест 1 пройден успешно!")


if __name__ == '__main__':
    test_1()
