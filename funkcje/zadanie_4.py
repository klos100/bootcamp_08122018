"Zaimplementuj funkcję formatującą podane napisy"


def formatowanie_tekstu(cena = 0,*args):
    napis = "\\".join(args)
    tekst_koncowy = napis.replace("$cena",str(cena))
    # for k in kwargs:
    #     tekst_koncowy = kwargs[k](napis,"$cena","10")
    return tekst_koncowy

print(formatowanie_tekstu(10,'koszt $cena PLN', 'kwota $cena brutto'))

def test_formatowanie_tekstu_bez_znacznikow():
    assert formatowanie_tekstu('',"nie $cena pojecia") == "nie  pojecia"


def formatuj(*napisy, **zmienne):
    napis = "\\".join(napisy)
    for zmienna in zmienne:
        napis = napis.replace(f"${zmienna}",zmienne[zmienna])
    return napis

def test_formatuj():
    assert formatuj("Hello $name $lastname", name="John", lastname = "Dupa") == "Hello John Dupa"