"""
Реализуйте функцию convert(), которая принимает один аргумент:
 - string — произвольная строка
Функция должна возвращать строку string:
 - полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
 - полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
 - полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.
"""


def convert(input_string):
    cnt_lower = 0
    cnt_upper = 0
    for symbol in input_string:
        if symbol.isalpha():
            if symbol.islower():
                cnt_lower += 1
            elif symbol.isupper():
                cnt_upper += 1
        else:
            continue
    print(cnt_lower, cnt_upper)
    return input_string.lower() if cnt_lower >= cnt_upper else input_string.upper()
