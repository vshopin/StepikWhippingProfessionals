"""
Напишите программу с использованием декоратора, которая переопределяет функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.
"""


def uppercase(func):
    def wrapper(*args, **kwargs):
        args = [str(i).upper() for i in args]
        kwargs = {k: str(v).upper() for k, v in kwargs.items()}
        return func(*args, **kwargs)

    return wrapper


print = uppercase(print)
print('hi', 'there', end='!')
