import pytest
def silnia(x):
    if x <0:
        raise ValueError ("Argument musi być > od zera")
    if x == 0:
        return 1
    else:
        return x* silnia(x-1)




def dodaj(liczba):
    if liczba == 0:
        return 0
    else:
        return liczba + dodaj(liczba-1)

print(dodaj(5))


print(silnia(5))


def test_silnia_dla_0():
    assert silnia(0) == 1

def test_silnia_dla_wiekszych_od_0():
    assert silnia(5) == 120

def test_argument_mniejszy_od_zera():
    with pytest.raises(ValueError) as e:
        silnia(-10)