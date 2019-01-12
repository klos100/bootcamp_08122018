tekst = 'Ala ma <kota>, a kot ma Alę'

n = tekst.find('<')
m = tekst.find('>')

print(len(tekst[n + 1:m]))

# drugi sposob:
dlugosc = 0

text1 = "Ala ma kota"
text2 = "Ala <ma> kota"
text3 = "Ala <> ma kota"

dlugosc = 0
licz = False
for znak in text2:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False
        break
    elif licz:
        dlugosc += 1

#assert dlugosc == 2
print(dlugosc)
