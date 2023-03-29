"""
Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
 :number - натуральное число
Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.
"""


def print_digits(number):
    str_number = list(map(int, str(number)))

    def req(num):
        if len(num) > 0:
            i = len(num) - 1
            print(num.pop(i))
            i -= 1
            req(num)

    req(str_number)


print_digits(4868569493888292933)
