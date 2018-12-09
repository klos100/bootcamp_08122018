znalezione_maksimum = None
znalezione_minimum = None
liczba = None

while True:
    komenda = input(f"Podaj liczbę lub [k] by zakończyć: ")
    if komenda == 'k':
        break
    if len(komenda) > 0 and komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("nie liczba")

    if liczba or liczba == 0:
        if znalezione_maksimum is None or znalezione_maksimum > liczba:
            znalezione_maksimum = liczba
        if znalezione_minimum is None or znalezione_minimum < liczba:
            znalezione_minimum = liczba

print("Znalezione max: ", znalezione_maksimum)
print("Znalezione mix: ", znalezione_minimum)
