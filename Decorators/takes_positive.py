"""
Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в декорируемую функцию,
являются положительными целыми числами.
Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
TypeError, если аргумент не является целым числом
ValueError, если аргумент является целым числом, но отрицательным или равным нулю
Примечание 1. Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или при наличии разных
аргументов, несоответствующих разным условиям: TypeError, затем ValueError.
"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        args1 = [(lambda x: x > 0)(x) for x in args]
        kwargs1 = [(lambda x: x > 0)(x) for x in kwargs.values()]
        args2 = [(lambda x: x % 1 == 0)(x) for x in args]
        kwargs2 = [(lambda x: x % 1 == 0)(x) for x in kwargs.values()]
        if all(args1) and all(kwargs1) and all(args2) and all(kwargs2):
            return func(*args, **kwargs)
        else:
            if not (all(args2) and all(kwargs2)):
                raise TypeError
            else:
                raise ValueError

    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))
