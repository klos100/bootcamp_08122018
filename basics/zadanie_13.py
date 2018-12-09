dni = input("Ilosc dni: ")

i = 0
temp = 0
while i < int(dni):
    komenda = input(f"Podaj temperaturę w dniu {i+1} lub [k] by zakończyć: ")
    if komenda == 'k':
        break
    temp_i = float(komenda)
    temp += float(temp_i)
    i += 1

srednia = int(temp) / i

print(srednia)
