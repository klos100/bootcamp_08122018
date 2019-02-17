"""Napisz program obslugujacy baze danych pracownikow. W bazie danych przechowuje imię, nazwisko,
 email, rok urodzenia, pensję. Skorzystaj z modułu json"""
import json
import getpass

wybor = input("Co chcesz zrobić? [d - dodaj, w - wypisz]:")

try:
    with open("zadanie_1.json") as fp:
        lista_pracownikow = json.load(fp)
except FileNotFoundError:
    lista_pracownikow = []

def dodaj_pracownika(lista_pracownikow):
    imie = input("Podaj imię pracownika: ")
    nazwisko = input("Podaj nazwisko pracownika: ")
    rok_urodzenia = input("Podaj rok urodzenia pracownika: ")
    pensja = input("Podaj wielość wynagrodzenia pracownika: ")

    pracownik = {"imie": imie, "nazwisko": nazwisko, "rok_urodzenia": rok_urodzenia, "pensja": pensja}
    lista_pracownikow.append(pracownik)

    with open("zadanie_1.json", 'w') as fp:
        json.dump(lista_pracownikow, fp)


def wypisz_pracownika(lista_pracownikow):
    for nr, pracownik in enumerate(lista_pracownikow,start = 1):
        print ('Ok')#(f"- [ {nr}] {lista_pracownikow['imie']} {lista_pracownikow['nazwisko']}")



def usun_pracownika(pracownicy):
    nr =  input("Ktorego pracownika usunąć")
    haslo = getpass.getpass("Podaj haslo")
    if haslo != 'Tajne':
        print("zle haslo")
        return

    del lista_pracownikow[int(nr)-1]

    with open("zadanie_1.json", 'w') as fp:
        json.dump(lista_pracownikow, fp)


if wybor == 'd':
    dodaj_pracownika(lista_pracownikow)
elif wybor == 'w':
    wypisz_pracownika(lista_pracownikow)
elif wybor == "u":
    wypisz_pracownika(lista_pracownikow)
    usun_pracownika(lista_pracownikow)

