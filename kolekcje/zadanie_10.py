slowo = input("Podaj slowo: ")

slownik  = {}
slownik2 = {}
for i in slowo:
    ilosc = slowo.count(i)
    if i not in slownik:
        slownik[i] = ilosc

for k,v in slownik.items():
    print (f"Litera {k} wystepuje {v} razy")

# lub:

#d = dict([slowo.count(a) for a in slowo])
#print (f"Slownik, proba : {d}")

for z in slowo:
    slownik2[z] = slownik2.get(z,0)+1
print (f"Slownik, proba : {slownik2}")

from collections import defaultdict

#lambda = to wartość domyślna

