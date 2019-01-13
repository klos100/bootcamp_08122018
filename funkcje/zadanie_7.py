lista = [1, 2, 3, 4, 5, 6, 7]


def przytnij(data, start, stop):
    # dokumentacja funkcji   -piszesz trzy cudzyslowy i enter i samo wchodzi
    """
    Przycina liste o zadana funkcje
    :param data: list
    :param start: function
    :param stop: function
    :return: list
    """
    wynik = []
    for i in data:
        if start(i):
            wynik.append(i)
            if stop(i):
                break
    return wynik


print(przytnij(lista, start = lambda x: x > 3, stop = lambda x: x == 6))
#print(przytnij(lista(range(1000)), start = lambda x: x > 100, stop =lambda x: x % 11 == 0))


def test_przytnij():
    wynik = przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 6)
    assert wynik == [4, 5, 6]

def test_przytnij():
    wynik = przytnij(
        data=[1, 2, 3, 4, 5, 6, 7],
        start=lambda x: x > 3,
        stop=lambda x: x == 8)
    assert wynik == [4, 5, 6, 7]

