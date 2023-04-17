"""
Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время ее выполнения,
а именно: имя функции, переданные аргументы и возвращаемое значение в следующем формате:
TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции,
а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
"""
import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        result = (func(*args, **kwargs))
        if type(result) == str:
            print(f"TRACE: возвращаемое значение {func.__name__}(): '{result}'")
        else:
            print(f"TRACE: возвращаемое значение {func.__name__}(): {result}")
        return result

    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')