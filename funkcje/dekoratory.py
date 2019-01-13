

def loguj_uzycie(func):
    """To bedzie dekorator. Wypisze tekst przed i po uruchomieniu funkcji"""
    def wrapper(*args,**kwargs):
        print("To sie wykona przed")
        func(*args,**kwargs)
        print("To się wykona po")
    return wrapper

@loguj_uzycie
def pobierz_dane():
    print("Pobralem dane")

print("Nie udekorowane")
pobierz_dane()
print()

print("Udekorowane")

#pobierz_dane = loguj_uzycie(pobierz_dane)

pobierz_dane()

@loguj_uzycie
def potega(podstawa,wykladnik):
    wynik = podstawa**wykladnik
    return wynik

print(potega(2,3))