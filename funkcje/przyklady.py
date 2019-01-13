liczby = [1,8,3,4,5]
liczby2 = [5,6,8,3]

# for i,l in enumerate(liczby):
#     print(f"Indeks = {i}, wartosc = {l}")

def drukuj(liczby):
    for i, l in enumerate(liczby):
        print(f"Indeks = {i}, wartosc = {l}")

drukuj(liczby)
print()
drukuj(liczby2)
print()

def wykonaj_operacje (operacja, *args):
    print(type(args))
    return operacja(args)

print(wykonaj_operacje (min, 10,20,30,46))
print(wykonaj_operacje (max, 10,20,30,46))
print(wykonaj_operacje (sum, 10,20,30,46))

def hello():
    return "Hello!"

def hi():
    return "Hi"

def przywitaj_sie(funcion):
    print(funcion)

przywitaj_sie(hi)
przywitaj_sie(hello)


def sprawdz_czy(x,funkcja1,funkcja2):
    return funkcja1(x) and funkcja2(x)

print(sprawdz_czy(10,lambda x: x<11, lambda x: x%2 ==0))

def sprawdz_czy_podzielna_przez_2_3(x):
    return x%2 == 0 and x%3 == 0

print(sprawdz_czy(12,sprawdz_czy_podzielna_przez_2_3, lambda x: x>5))