miasto_a = input("Podaj miasto A : ")
miasto_b = input("Podaj miasto B: ")
dystans = input (f"Podaj dystans {miasto_a} - {miasto_b}: ")
cena_paliwa = input ("Podaj cenę paliwa: ")
spalanie = input ("Podaj spalanie: ")

dystans = float(dystans)
cena_paliwa = float(cena_paliwa)
spalanie = float(spalanie)
print()
koszt_przejazdu = (dystans/100)*spalanie*cena_paliwa

#print (koszt_przejazdu)

info = f'Koszt przejazdu {miasto_a} - {miasto_b} to {koszt_przejazdu} PLN'

print (info)