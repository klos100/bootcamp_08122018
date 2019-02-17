import datetime
import json

print(datetime.date.today())

datetime.date(2019,7,2) # ustawiaomy na jakas datę

a = datetime.datetime.today()
print(a)

b = a + datetime.timedelta(days=2)
print(b)

import decimal

# ulamki dziesietne

decimal.Decimal(1)
c = decimal.Decimal(100000000000000000001)
print(c)

d = decimal.Decimal('100000000000000000001.01') # trzeba zapisac w stringu bo inaczej pajton potraktuje to jako float
#  i obetnie do pietnastego znaku
print(d)

s = '{"kwota":1.56}'
json.loads(s)
e = json.loads(s,parse_float=decimal.Decimal)
print (e)



with open(r'C:\Program Files (x86)\Microsoft Office\Stationery\1033\CURRENCY.GIF', 'rb') as f:
    img = f.read()

import struct

struct.unpack('<HH', img[6:10]) # literki odpowiedzialne za bajty a img odcina nam ilosc bajtow - od 6 do 10 bajtu
Out[4]: (800, 232)
# domyslnie duze litery dla binarnych bo tam nie ma wartosci minusowych, czyli sa unsigned

struct.unpack('<ccccccHH',img[:10]) #ccc ccc H H to 1 bajt, 1 bajt, 2 bajty, 2 bajty (czytane z nagłowka gifa - z netu)
Out[6]: (b'G', b'I', b'F', b'8', b'9', b'a', 800, 232)

