"""
Написать функцию, которая принимает в качестве аргументов 3 числа, и возвращает функцию выводящюю квадратное уровнение:
f(x)=a(x**2)+bx+c
"""


def generator_square_polynom(a, b, c):
    def test(x):
        return a * (x ** 2) + b * x + c

    return test


f = generator_square_polynom(1, 2, 1)
print(f(5))
