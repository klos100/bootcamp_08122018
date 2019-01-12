slowo = input("Podaj słowo: ")

samogl = 'aoeiuy' #lepiej, zeby tę zmienna napisać dużymi literami,bo duzymi literami piosze się zmienne stale

n = 0
for i in slowo:
    if i in samogl:
        n += 1

m= 0
for samogloska in samogl:
    m += slowo.lower().count(samogloska)

print(f"Liczna samoglosek w podanym slowie: {n}")
print (m)

