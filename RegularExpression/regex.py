import re

input_string = input()
match = re.search(r'...\....', input_string)

print(match[0])
