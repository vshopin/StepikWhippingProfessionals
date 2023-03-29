"""
Реализуйте функцию power(), которая принимает один аргумент:
:degree — целое число
Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x и возвращает значение x в степени degree.
"""


def power(degree):
    def test(x):
        return x ** degree
    return test


square = power(2)
print(square(5))
