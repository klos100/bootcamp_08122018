lista = [2, 15, -10, 25, 7, -5, 0]

i = 0
j = 0

for n in lista:
    if n > 0:
        i += 1
    elif n < 0:
        j += 1

print(f"dodatnie: {i}")
print(f"ujemne: {j}")

# druga opcja

dodatnie = len([x for x in lista if x > 0])
ujemne = len([x for x in lista if x < 0])

print(f"dodatnie {dodatnie}, ujemne {ujemne}")
