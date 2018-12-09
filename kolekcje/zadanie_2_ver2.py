dane = input("podaj liczby, rozdziel je spacjami: ")
dane = dane.split()
print(dane)

dane2 = [int(d) for d in dane]
print(dane2)

dane3 = map(int, dane)
print(list(dane3))