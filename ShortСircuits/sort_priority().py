"""
Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:
 :values — список чисел
 :group — список, кортеж или множество чисел
Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу чисел из group, которая должна следовать первой.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию sort_priority(), но не код, вызывающий ее.
"""


def sort_priority(values, group):
    values.sort()
    test = sorted(group)
    test2 = []
    for i in range(len(test)):
        if test[i] in values:
            values.remove(test[i])
            test2.append(test[i])
    values[:] = test2 + values


numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)
