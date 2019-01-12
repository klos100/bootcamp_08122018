# STRING

napis = 'dnkwndl'
print(dir(napis))  # jakie metody sa dostepne dla obiektu

print(napis.endswith('dl'))

print("k" in napis)

print(napis.upper())

napis2 = "ala ma kota"#
print(napis2.capitalize())

print(napis2.title())

print(help(napis2.title)) #bez () na końcu niwe wywołujew mwtody tylko
print()

# SLOWNIK spr -> tablica haszujaca

#definiowanie pustego slownika
d = dict()
d['a'] = 5
d['b'] = 9
print (d)

print(dir(d)) #jakie ma metody slownik

print (d.keys())
print (d.values())
print (d.items()) #zwraca liste tupli

#inny sposob tworzenia slownika:
slownik2 = dict(a=1,b=2)
print(slownik2)


c = d.get('e',0) #szuka czy jest w slowniku dany klucz, po przecinku do ma wyrzucic jesli nie ma
print(c)

# ZBIOR

zbior ={1,2,3}
zbior.add(4)
print (zbior)

print(len(zbior))

a = set([1,2,3])
b = {2,3,4}
print(a|b)
print(a-b)
print(a&b)
print(a^b)


