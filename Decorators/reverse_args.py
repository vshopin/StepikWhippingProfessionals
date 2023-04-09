"""
Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую функцию func в обратном порядке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""


def reverse_args(func):
    def wrapper(*args, **kwargs):
        args = [i for i in args][::-1]
        kwargs = {k: v for k, v in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper


@reverse_args
def operation(a, b, name):
    return a // b + name


print(operation(10, 90, name=1))
