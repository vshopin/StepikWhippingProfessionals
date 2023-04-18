"""
Реализуйте декоратор repeat, который принимает один аргумент:
times — натуральное число
Декоратор должен вызывать декорируемую функцию times раз.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times -1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper

    return decorator


@repeat(10)
def add(a, b):
    '''sum of two numbers'''
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))
