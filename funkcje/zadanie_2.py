def wiecej_niz (tekst,ilosc):
    a = set()
    tekst_set = set(tekst)
    for i in tekst_set:
        if tekst.count(i)> ilosc:
            a.add(i)
    return a

print(wiecej_niz('domdomdom podloga',2))

def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale',3) == {'a',' '}

def nowe(tekst,ilosc):
    napis = set(tekst)
    return {i for i in napis if tekst.count(i)> ilosc}

print('nowe',nowe('dmokmmdkk',2))

def potega(podstawa,wykladnik=2): #jeli nie podam to domyslnie bedzie podnosil do potegi 2
    return podstawa**wykladnik

print(potega(2,3))
print(potega(2))


def foo (a,b,c,d=1,e=1): # funkcja musi miec 3 arguenty, zeby poszła
    pass