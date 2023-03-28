"""
Реализовать функцию которая выведет на экран треугольник из звездочек, так чтобы основание треугольника была вверху
На вход подается h - высота
"""


def triangle(height):
    n = height

    def req(num):
        if num >= 1:
            print('*' * num)
            req(num - 1)

    req(n)


h = int(input())
triangle(h)
