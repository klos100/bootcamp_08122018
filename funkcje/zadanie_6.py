"zaimplementuj funkcję splaszczajac podaną listę"

lista = [1, 2, 3, 4, [5, [6], 7]]


def splaszcz(lista):
    wynik = []
    for i in lista:
        if isinstance(i, list):
            for ii in splaszcz(i):
                wynik.append(ii)
        else:
            wynik.append(i)
    return wynik


print(splaszcz(lista))


def test_splaszcz_pusta_lista():
    assert splaszcz([]) == []


def test_splaszcz_plaska_lista():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]


def test_splaszcz_zagniezdzona_lista():
    assert splaszcz([1, 2, [3, 4]] == [1, 2, 3, 4])
    assert splaszcz([1,2,3,[4,5,[6]],7]) == [1,2,3,4,5,6,7]