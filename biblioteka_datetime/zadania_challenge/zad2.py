from string import ascii_letters

with open(r"C:\Users\kurs\workspace\biblioteka_datetime\zadania_challenge\dane.txt") as f:
    dane = f.read()

out = []

for z in dane:
    if z in ascii_letters:
        out.append(z)

print(out)
print("".join(out))


import re
pattern = re.compile("[a-zA-Z]")
print("rozwiazanie wyrazeniami reg")
print(pattern.findall(dane))

print(ord('a'))
print(chr(122))