
"""Naspisz funkcje, która przyjmnie dowolną liczbę napisów1. zwróci te napisy połączone znakiem nowej linii
>>> napisy('a','b')
a
b
>>> napisy('a','b','d')
a
b
d
"""

def napisy(*args, **kwargs):
    tekst = "\n".join(args)
    for k in kwargs:
        tekst = kwargs[k](tekst)

    # if funkcja:
    #     tekst = funkcja(tekst)
    # return tekst

def upper (napis):
    return napis.upper()


print(napisy('a','b'))
print()
print(napisy('a','b','d'))
print()
print(napisy('a','b','d',funkcja = upper))
print(napisy('a','h','e',funkcja = str.upper))
print(napisy('a','h','e',funkcja = str.upper,funkcja2=str.title))

