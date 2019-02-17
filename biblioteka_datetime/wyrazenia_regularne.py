import re

s = "Ala ma kota! Kot ma ale. Kot lubi mleko. Nie lubi ryb."

print(re.findall('lubi', s))  # wyszukiwanie

print(re.findall('lubi .', s))  # do . pasuje dowolna litera

print(re.findall('... ma', s))

print(re.findall('.{3} ma', s))  # dowolny znak razy 3

print(re.findall('\w{3} ma', s)) #dowolnw 3 znaki alfanumeryczne

print(re.findall(r'\w+', s)) #ignoruje znaki szczegolne

print(re.findall(r'[A-Z].*\.', s)) #* tyle znakow ile sie da; dowolny znak ile znakow sie da, az do ,


print(re.findall(r'[A-Z].*?[\.\!]', s)) # ? - wez jak najmniej, zeby spelnic regulę i wykrzyknik dodalismy do stoperow
# (w kwadratowyn nawiasie)

print(re.findall(r'([A-Z]\w*)\W.*?[\.\!]', s))