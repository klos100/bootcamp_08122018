i = 10
lista = []

for i in range(0, 10):
    liczba = input("Podaj liczbę lub [k] by zakończyć: ")
    if liczba == 'k':
        break
    lista.append(int(liczba))

srednia = sum(lista) / len(lista)

print(srednia)
