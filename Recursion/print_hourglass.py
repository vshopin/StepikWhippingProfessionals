"""
Написать программу с использованием рекурсивной функции, которая выводит изображение песочных часов, составленное из
цифр 1, 2, 3, 4.
"""


def print_hourglass():
    def rec(number, space, count):
        if number < 5:
            print(' ' * space + str(number) * count)
            rec(number+1, space+2, count-4)
            if number != 4: print(' ' * space + str(number) * count)
    rec(1, 0, 16)


print_hourglass()
