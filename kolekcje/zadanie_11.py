liczby = input("Podaj liczby po przecinku: ")
liczby_parzyste = set(range(0, 100, 2))

liczby = liczby.split(",")
liczby = [int(i) for i in liczby]
liczby_uzytkownik = set(liczby)
unikalne_liczby = len(liczby_uzytkownik)
ilosc_przystych = len(liczby_parzyste & liczby_uzytkownik)

print(f"Ilosc liczb unikalnych: {unikalne_liczby}, w tym liczby parzyste: {ilosc_przystych}")


# inne:
liczbyy = set()
while True:
    komenda = input("Podaj liczbę lub k by zakonczyc:")
    if komenda == 'k':
        break
    else:
        liczbyy.add(int(komenda))
print("Liczby:", len(liczbyy))
print("z czego przystych jest:", len(liczbyy&liczby_parzyste))

