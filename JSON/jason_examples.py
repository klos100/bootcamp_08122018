import json

lista = [1, 2, 3, 'a', 'b', 'c']

# uzycie bibloteki i metody, która przetworzy listę na napis json
# serializacja
json_list = json.dumps(lista)

print(type(json_list))


napis = '{"1":"a","2":"b"}'

# deserializacja - przejjscie z jasona do pytohna

ds_napis = json.loads(napis)
print (ds_napis)

print(type(ds_napis))

print(help(json.dump))   # zapis do pliku ale w formiacie json

with open("napis.json", 'w') as fp:
    json.dump(ds_napis,fp)

# odczyt pliku w formiacie json

with open("napis.json") as fp:
    ob = json.load(fp)
    print(ob)
    print(type(ob))