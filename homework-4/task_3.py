"""
Задание 3 (необязательное).
Итератор FlatIterator для обработки списков с любым уровнем вложенности.
"""


class FlatIterator:
    """
    Итератор для преобразования вложенных списков любого уровня в плоскую последовательность.
    """

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.stack = [iter(self.list_of_list)]
        return self

    def __next__(self):
        while self.stack:
            try:
                # Пытаемся получить следующий элемент из текущего итератора
                item = next(self.stack[-1])
                
                # Если элемент - список, добавляем его итератор в стек
                if isinstance(item, list):
                    self.stack.append(iter(item))
                else:
                    # Если не список, возвращаем элемент
                    return item
            except StopIteration:
                # Если текущий итератор исчерпан, удаляем его из стека
                self.stack.pop()
        
        # Если стек пуст, все элементы пройдены
        raise StopIteration


def test_3():
    """
    Тестовая функция для проверки работы FlatIterator с любым уровнем вложенности.
    """
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    
    print("Тест 3 пройден успешно!")


if __name__ == '__main__':
    test_3()
