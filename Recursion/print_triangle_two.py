"""
Реализовать функцию, которая выведет на экран треугольник из звездочек, так чтобы основание треугольника была внизу
На вход подается h - высота
"""


def triangle(height):
    if height > 0:
        triangle(height - 1)
        print('*' * height)


h = int(input())
triangle(h)
