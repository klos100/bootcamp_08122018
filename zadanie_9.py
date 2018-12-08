import datetime

wiek = int(input("Podaj datę urodzenia: "))

rok = (datetime.datetime.now().year)

if rok - wiek >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Niestety nie kupisz piwa :(")
