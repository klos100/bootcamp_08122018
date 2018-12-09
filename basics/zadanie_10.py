liczba_1 = int(input("Podaj pierwszą liczbę: "))
liczba_2 = int(input("Podaj drugą liczbę: "))
operator = input("Podaj rodzaj operacji: ")

if operator == "+":
    wynik = liczba_1 + liczba_2
elif operator == "-":
    wynik = liczba_1 - liczba_2
elif operator == "*":
    wynik = liczba_2 * liczba_1
elif operator == "/":
    if liczba_2 == 0:
        print ("Operacja niedozwolana")
    else:
        wynik = liczba_1 / liczba_2
else:
    wynik = "Nie rozpoznaję operatora"

print(f"Wynik: {wynik}")


print (eval(f"{liczba_1}{operator}{liczba_2}"))