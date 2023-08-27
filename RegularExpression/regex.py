import re

input_string = input()
match = re.findall(
    r'[A-Z]{1,2}\d[A-Z\d]? \d[ABD-HJLNP-UW-Z]{2}', input_string)

print(match)
