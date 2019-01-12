produkty = {'ziemniaki': 2.25,
            'brukselka': 1.25,
            'szczypiorek': 2}

magazyn = {'ziemniaki': 10,
           'brukselka': 10,
           'szczypiorek': 10}

while True:
    rola = input("Czy jestes klientem [k] ,czy dostawca [d], [q] by zakonczyc: ")
    if rola.lower() in ['klient', 'k']:
        while True:
            print("Nasz skleop oferuje:")
            for zakup, cena in produkty.items():
                print(f"- {zakup} - {cena:.2f}")

            print()
            produkt = input("Podaj produkt, [k] by zakonczyc:")
            if produkt.lower() == 'k':
                print("Zapraszamy ponownie")
                break
            waga = float(input(f"Ile chcesz kupic - {produkt}: "))
            if waga > magazyn[produkt]:
                print()
                print("Nie ma tyle w magazynie")
                print(f"W magazynie zostało: {magazyn[produkt]}")
                print()
            else:
                cena = produkty.get(produkt)
                if cena:
                    koszt = produkty[produkt] * waga
                    print(f"Płacisz: {koszt}")
                    magazyn[produkt] = float(magazyn[produkt]) - waga  # lub
                    print()
                else:
                    print("Nie ma")
    elif rola.lower() in ['dostawca', 'd']:
        do_dodania = input("Dodaj nowy produkt, jego ilosc i cenę: [nazwa ilosc cena ")
        if len(do_dodania.split()) == 3:
            nazwa, ilosc, cena = do_dodania.split() # dzieli po bialych znakach
            ilosc = float(ilosc)
            cena = float(cena)
            produkty[nazwa] = cena
            magazyn[nazwa] = magazyn.get(nazwa, 0) + ilosc
            print("Dziękuję, produkt dodany")
        else:
            print("Nie poprawny produkt")

    elif rola.lower() == 'q':
        print("Program przestaje działąć")
        break
