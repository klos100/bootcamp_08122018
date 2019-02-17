class Konwerter:
    def cel_to_farh(self, cel):
        result = cel * 9 / 5 + 32
        return result

    def farh_to_cel(self, farh):
        result = round((farh - 32) / 1.8, 2)
        return result


assert Konwerter().farh_to_cel(32) == 0
assert Konwerter().cel_to_farh(0) == 32
assert Konwerter.cel_to_farh(None, 0) == 32  # None jest argumentem self, bo jak jest w klasie potrzeba


### slownik z porządkiem

from collections import OrderedDict

### wtedy --> slownik = OrdereDict([(tupla),(tupla),(tupla)])

