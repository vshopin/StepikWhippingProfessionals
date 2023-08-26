import re

input_string = input()
match = re.findall(
    r'\d{2}\.\d{2}\.\d{4}|\d{2}\/\d{2}\/\d{4}|\d{4}\.\d{2}\.\d{2}|\d{4}\/\d{2}\/\d{2}', input_string)

print(match)
