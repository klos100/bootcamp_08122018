import re

pattern = re.compile("[a-z][A-Z]{3}([a-z]){1}[A-Z]{3}[a-z]")

with open ("dane_3.txt") as f:
    dane = f.read()


wynik = pattern.findall(dane)
print(wynik)