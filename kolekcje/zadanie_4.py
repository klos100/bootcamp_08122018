i = 0

lista = []

for n in range(0,101):
    if n%3 == 0 or n%5 == 0:
        i+=1
        lista.append(n)
        print (n)

print(f"W przedziale jest : {i}")
print ([x for x in lista])
print (len(lista))