class Postac:

    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self.zdrowie = zdrowie
        self.max_zdrowie = zdrowie
        self._atak = atak
        self.ekwipunek = []

    @property
    def atak(self):
        a = self._atak + sum([e.bonus_do_ataku for e in self.ekwipunek])
        return a

    def otrzymaj_obrazenia(self, obrazenia):
        print(f'{self.imie} oberwał za {obrazenia} obrażeń.')
        self.zdrowie -= obrazenia
        if self.zdrowie < 0:
            self.zdrowie = 0

    def wylecz(self, pkt_zdrowie):
        if self.zdrowie == 0:
            return False
        self.zdrowie += pkt_zdrowie
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = self.max_zdrowie

    def dodaj_przedmiot(self, przedmiot):
        self.ekwipunek.append(przedmiot)

    def zabierz_przedmiot(self, przedmiot):
        self.ekwipunek.remove(przedmiot)

    def moc_ataku(self):
        return random.randint(self.atak // 2, self.atak)

    def __str__(self):
        napis = f'Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia. \nEKWIPUNEK: '
        for przedmiot in self.ekwipunek:
            napis += f'{przedmiot.nazwa}, {przedmiot.bonus_do_ataku} do ataku'
        return napis
