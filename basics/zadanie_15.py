from random import randint

x = randint(1, 10)
y = randint(1, 10)
print(x)
print(y)

xs = randint(1, 10)
ys = randint(1, 10)
print(xs)
print(ys)

kroki = abs(xs - x) + abs(ys - y)

liczba_krokow = 0

DEBUG = True

while True:

    kroki_przed_ruchem = abs(xs - x) + abs(ys - y)
    print(f"Twoja pozycja to: {x},{y}")
    if DEBUG:
        print("DEGUG info:")
        print (f"Pozycja skarbu to: {xs},{ys}")
        print ("Minimalan ilosc krokw", kroki)
    kierunek = input("Podaj kierunek w-góra, s-dół ,a-lewo, d-prawo: ")
    if kierunek == 'w':
        y += 1
    elif kierunek == 's':
        y -= 1
    elif kierunek == 'a':
        x -= 1
    elif kierunek == 'd':
        x += 1
    liczba_krokow += 1
    kroki_po_ruchu = abs(xs - x) + abs(ys - y)

    if x<1 or y<1 or x>10 or y>10:
        print ("Koiec gry")
        break

    if x == xs and y == ys:
        print("Wygrales!")
        print("Minimalan liczba kroków wynosiła: ", liczba_krokow)
        break

    los = randint(1,5)
    if los != 3:
        if kroki_po_ruchu < kroki_przed_ruchem:
            print("Cieplo")
        else:
            kroki_po_ruchu > kroki_przed_ruchem
            print("Zimno")

    if liczba_krokow >= kroki*2:
        xs = randint(1, 10)
        ys = randint(1, 10)
        kroki = abs(xs - x) + abs(ys - y)
        liczba_krokow = 0
        print("Skarb zmienił położenia")
        print()

# krok_x = input("Podaj x: ")
# krok_y = input("Podaj_y: ")
#
# if y > ys and x > xs:
#     print("do gory w lewo")
# elif y < ys and y < ys:
#     print("na dol na lewo")
#
# print("Liczba kroków: ", kroki)
