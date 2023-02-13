import re

text = "Paul Macarnin es un humano"

pattern = r"Paul [A-Z]\w+"

matches = re.finditer(pattern, text)

for match in matches:
    print(match)
