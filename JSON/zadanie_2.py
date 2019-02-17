import requests
import decimal

resp = requests.get("http://api.nbp.pl/api/exchangerates/tables/A?format = json")

kursy = resp.json(parse_float=decimal.Decimal) # zeby wartosci walut były dokladniejsze

for r in kursy[0]['rates']:
    if r['currency'] == 'euro':
        print(r)


print("Dusponuję walutami:")

for r in kursy[0]['rates']:
    print (r)

waluta = input("podaj kod waluty ktora chcesz kupic: ")
za_ile = decimal.Decimal(input("Za ile: ")) # wczesniej zamiast decimal.Decimal bylo float

for k in kursy[0]['rates']:
    if k['code'] == waluta:
        print(f"Za {za_ile} PLN mozesz kupic {za_ile/k['mid']:.2f} {waluta}")
