tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(tupla[1])
print(tupla[-2])
print(tupla[2:8])
print(tupla[::3])
print(tupla[::-2])
print(tupla[-2::-2])

lista = [1,2,3,4]
lista.append("a")
print(lista)

lista.extend(["a","b"])
print (lista)

print("jak dziala pop")
print (lista.pop())
print (lista)
# usuwa ostatni element listy i usuwa z listy

print("Sortowanie listy")
lista2 =[1,2,5,9,2]
print (lista2.sort())
print(lista2)
posortowane = sorted(lista2)
print (posortowane)
