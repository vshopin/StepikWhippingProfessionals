"""
Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:
start — неотрицательное целое число
end — неотрицательное целое число
char — одиночный символ, по умолчанию равный точке .
Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы в диапазоне индексов от start
(включительно) до end (не включительно) на символ char.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
Примечание 2. Гарантируется, что start < end.
"""
import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = list(func(*args, **kwargs))
            if len(result) < start:
                return ''.join(result)
            for i in range(start, end):
                result[i] = char
                if i == len(result) - 1:
                    break
            return ''.join(result)

        return wrapper

    return decorator


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())
