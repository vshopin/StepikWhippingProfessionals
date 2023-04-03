"""
Реализуйте декоратор sandwich, который выводит тексты:

---- Верхний ломтик хлеба ----
---- Нижний ломтик хлеба ----
до и после вызова декорируемой функции соответственно.
"""


def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result

    return wrapper


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())
