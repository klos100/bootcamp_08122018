def czy_jest_pierwsza(liczba):
    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True


print(czy_jest_pierwsza(12))

# assert czy_jest_pierwsza(17) == True
# assert czy_jest_pierwsza(10) == False

# lub:

assert czy_jest_pierwsza(17)
assert not czy_jest_pierwsza(10)
