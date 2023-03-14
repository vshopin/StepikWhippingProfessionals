"""
Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:
- состоит из 4, 5 или6 символов
- состоит только из цифр (0−9)
- не содержит пробелов
Реализуйте функцию is_valid(), которая принимает один аргумент:
 - string — произвольная строка
Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, или False в противном случае.
"""


def is_valid(input_string):
    return all((4 <= len(input_string) <= 6, input_string.isdigit()))


assert True == is_valid('4367')
assert True == is_valid('92134')
assert False == is_valid('')
assert False == is_valid('89abc1')
assert False == is_valid('49 36')
