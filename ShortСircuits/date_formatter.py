"""
Реализуйте функцию date_formatter(), которая принимает один аргумент:
:country_code — код страны
Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату (тип date) и возвращает строку с данной датой в формате страны с кодом country_code.
"""
from datetime import date


def date_formatter(country_code):
    def date_short(date_format):
        country_code_format_dict = {'ru': '%d.%m.%Y',
                                    'us': '%m-%d-%Y',
                                    'ca': '%Y-%m-%d',
                                    'br': '%d/%m/%Y',
                                    'fr': '%d.%m.%Y',
                                    'pt': '%d-%m-%Y', }
        for key in country_code_format_dict.keys():
            if country_code == key:
                return date_format.strftime(country_code_format_dict[key])

    return date_short


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))
