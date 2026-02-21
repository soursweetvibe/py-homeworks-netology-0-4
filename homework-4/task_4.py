"""
Задание 4 (необязательное).
Генератор flat_generator для обработки списков с любым уровнем вложенности.
"""
import types


def flat_generator(list_of_list):
    """
    Генератор для преобразования вложенных списков любого уровня в плоскую последовательность.
    """
    for item in list_of_list:
        if isinstance(item, list):
            # Если элемент - список, рекурсивно обрабатываем его
            yield from flat_generator(item)
        else:
            # Если не список, возвращаем элемент
            yield item


def test_4():
    """
    Тестовая функция для проверки работы flat_generator с любым уровнем вложенности.
    """
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)
    
    print("Тест 4 пройден успешно!")


if __name__ == '__main__':
    test_4()
