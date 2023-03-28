"""
Написать программу с использованием рекурсии, которая выводит последовательность натуральных чисел от 1 до 100
включительно
"""


def print_one_to_onehundred():
    n = 1

    def req(num):
        if num <= 100:
            print(num)
            req(num + 1)

    req(n)


print_one_to_onehundred()
