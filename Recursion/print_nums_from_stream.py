"""
Дана последовательность целых чисел. Написать программу с использованием рекурсии, которая выводит эту
последовательность в обратном порядке.
"""
import sys


def print_from_stream(stream):
    n = len(stream) - 1

    def req(num):
        if num >= 0:
            print(stream[num].strip('\n'))
            req(num - 1)

    req(n)


data = sys.stdin.readlines()
print_from_stream(data)
