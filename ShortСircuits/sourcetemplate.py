"""
Функция sourcetemplate() должна возвращать функцию, которая принимает произвольное количество именованных аргументов
и возвращает url адрес, объединенный со строкой запроса, сформированной из переданных аргументов.
При вызове без аргументов она должна возвращать исходный url адрес без изменений.

Примечание 1. Параметры в строке запроса должны располагаться в лексикографическом порядке ключей.
"""


def sourcetemplate(args):
    def test(**urls):
        if len(urls) == 0:
            result = args
            return result
        else:
            result = args + '?'
            for key, value in sorted(urls.items()):
                result += str(key) + '=' + str(value) + '&'
            return result[:len(result) - 1]

    return test


url = 'https://stepik.org/lesson/651459/step/14'
load = sourcetemplate(url)
print(load(thread='solutions', unit=648165))
