"""
Реализовать функцию которая выведет на экран треугольник из звездочек, так чтобы основание треугольника была вверху
На вход подается h - высота
"""


def triangle(height):
    if height >= 1:
        print('*' * height)
        triangle(height - 1)


h = int(input())
triangle(h)
