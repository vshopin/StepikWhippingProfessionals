"""
Реализуйте функцию same_parity(), которая принимает один аргумент:
 - numbers — список целых чисел
Функция должна возвращать новый список, элементами которого являются числа из списка numbers, имеющие ту же четность, что и первый элемент этого списка.
"""


def same_parity(numbers):
    return list(filter(lambda num: num % 2 == numbers[0] % 2, numbers))


assert [6, 0, 10, -20] == same_parity([6, 0, 67, -7, 10, -20])
assert [] == same_parity([])
assert [-7, 67, -9, -29] == same_parity([-7, 0, 67, -9, 70, -29, 90])

