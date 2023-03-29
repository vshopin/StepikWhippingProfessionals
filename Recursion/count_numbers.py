"""
Написать программу с использованием рекурсии, которая принимает на вход число и выводит количество цифр в этом числе.
"""


def print_count_of_numbers(n):
    if n < 10:
        return 1
    else:
        return 1 + print_count_of_numbers(n // 10)


num = int(input())
print(print_count_of_numbers(num))
