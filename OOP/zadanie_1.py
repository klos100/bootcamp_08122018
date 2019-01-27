"""Zaimplementuj klasę produkt przechowujaca info o cenie, nazwie i id prod.
Zaimplementuj metodę wypisujaca info na konsole"""


class Produkt:

    def __init__(self, cena, nazwa, id):
        self.cena = cena
        self.nazwa = nazwa
        self.id = id

    def print_info(self):
        print (f"Produkt: {self.cena}, id: {self.id}, cena: {self.nazwa}")

    def __str__(self):
        return f"Produkt: {self.cena}, id: {self.id}, cena: {self.nazwa}"


produkt = Produkt(1,"Woda",2.99)

produkt.print_info() #print

print(produkt) #return