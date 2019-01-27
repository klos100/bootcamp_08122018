class Osoba():

    def __init__(self,imie,nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        print(f"Czesc jestem {self.imie} {self.nazwisko}")

class Informatyk:
    pass

class Pracownik(Osoba,Informatyk):

    def __init__(self,imie,nazwisko,stanowisko):
        Osoba.__init__(self,imie,nazwisko)
        self.stanowisko = stanowisko

    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Pracuję jako {stanowisko}")

osoba = Osoba("adam","Dupa")
osoba.przedstaw_sie()

pracownik = ("Ania","Kowalska","trener")
