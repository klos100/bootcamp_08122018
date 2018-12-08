cena = 12
waga = 2.5
naleznosc = cena*waga

print ("Cena za kg: ", cena, end=', ')
print ("Waga: ",waga, end=', ')
print ("Należność: ", naleznosc)


# f print
info = f"""Cena za kg: {cena}, 
Waga: {waga}, 
Należność: {naleznosc}
"""

x = "{0},{1},{2}".format(cena,waga,naleznosc)

print (x)

print (info)

