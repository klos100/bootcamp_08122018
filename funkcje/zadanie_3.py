def policz_znaki(tekst, start='<', stop='>'):
    wynik = 0
    #czy_zliczac = False
    poziom = 0
    for znak in tekst:
        if znak == start:
            #czy_zliczac = True
            poziom += 1
        elif znak == stop:
            #czy_zliczac = False
            poziom -= 1
        elif poziom:
            wynik += poziom
    return wynik


# def policz_znaki(tekst, zn1='<', zn2='>'):
#     n, m = tekst.find(zn1), tekst.find(zn2)
#     ilosc = tekst.count(zn1, 0, m)
#     for i in range(0,)
#
#     return len(tekst[n + 1:m])


def test_policz_znaki_0_poziom():
    assert policz_znaki('ala ma kota a kot ma ale') == 0

def test_policz_znaki_1_poziom():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_1_poziom():
    assert policz_znaki('ala ma [kota] a kot ma ale') == 4

def test_policz_znaki_2_pozim():
    assert policz_znaki('ala [kota a kot] ma [ale]', '[', ']') == 13

def test_policz_znaki_2_pozim():
    assert policz_znaki('ala [kota [a kot]] ma ale', '[', ']') == 15

def test_policz_znaki_3_poziom():
    assert policz_znaki('a <a<a<a>>>') == 6
