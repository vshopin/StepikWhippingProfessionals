"""
В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, а оставшиеся размножаются,
и их становится в три раза больше. Так, количество лягушек k-й год может быть описано формулой:
Fk = 3(Fk-1 - 30)
Реализовать функцию с использованием рекурсии, которая принимает один аргумент year натуральное число.
Функция должна возвращать единственное число — количество лягушек в пруду в году
"""


def number_of_frogs(year):
    if year == 1:
        return 77
    else:
        return 3 * (number_of_frogs(year - 1) - 30)


num = int(input())
print(number_of_frogs(num))
