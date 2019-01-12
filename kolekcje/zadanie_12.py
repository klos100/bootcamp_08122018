lista = [9, 1, 6, 8, 2, 3, 0]

min = None

for j in range(0, len(lista)):
    ind = j
    for i in range(j, len(lista)):
        if min is None:
            min = lista[i]
        else:
            if lista[i] < min:
                min = lista[i]
                ind = i
    lista[j], lista[ind] = lista[ind],lista[j]

print(lista)


for i in range(len(lista)):
    indeks_min = i
    for j in range(i,len(lista)):
        if lista[j] < lista[indeks_min]:
            indeks_min = j
    lista[i], lista[indeks_min] = lista[indeks_min], lista[i]

print(lista)