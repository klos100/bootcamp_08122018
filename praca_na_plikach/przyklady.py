with open("readme.txt", encoding="utf-8") as f:  # 'r' jest domyslnie jak nie podamy to bedzie do odczytu
    print(f.read())
# pycharm ma kodowanie utf-8 a windows cp 1250

with open("readme.txt", "r") as f:  # 'r' jest domyslnie jak nie podamy to bedzie do odczytu
    for line in f:
        print(len(line))

print("druga metoda")
with open("readme.txt", "r") as f:  # 'r' jest domyslnie jak nie podamy to bedzie do odczytu
    for line in f.readlines():
        print(len(line))

with open("readme3.txt", 'w') as f:  # tworzy plik i zapisuje lub nadpisuje jak plik istnieje
    f.write("Ala ma kota")

with open("readme3.txt", 'a') as f:  # dopisuje do pliku
    f.write("\nKot ma alę")

