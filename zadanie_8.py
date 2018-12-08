dlugosc = float(input("Podaj długość opakowania: "))
wysokosc = float(input("Podaj wysokosc opakowania: "))
szerokosc = float(input("Podaj szerokosc opakowania: "))

objetosc = dlugosc * szerokosc * wysokosc

wynik = f"""objetosc: {objetosc}, 
większa do 1 litra: {objetosc>1000}"""

print(wynik)

if objetosc > 1000:
    print("Objętość jest większa niż 1 litr")
else:
    print("Objętość jest mniejsza niż 1 litr")
