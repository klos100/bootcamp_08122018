"""Napisz program znajdujacy w dostarczonym pliku wszystkie wystapienia:
- kodow pocztowych - 12-123; adresow email - test@email.com; dat - 12 Jan 1990"""

import re

with open("input.txt") as f:
    input = f.read()

print(re.findall(r'\b(\d{2}[\-]\d{3})\b', input)) #\b ograniczniki slowa koncowki wytrazenia

print(re.findall(r'\S+[\@].*?\.\w*?[\s]', input)) # + plus oznacza 1 i wiecej razy \S - dowolne znaki niespacjowe

print(re.findall(r'[\w\-+.]+@[\w\-.]+', input)) #przed malapa i po conajmniej jedno wystapienie tego co w nawiasach

print(re.findall(r'\d{2} \w{3} \d{4}',input))

print(re.findall(r'\b\d{1,2}\s[A-Z][a-z]{2}\s\d{4}\b',input)) #jeden lub dwa przy dniu; \b pilnuje konca wyrazu