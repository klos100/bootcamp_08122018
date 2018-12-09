liczby = [5, 2, 1, 4, 3]
temp = liczby[0]

# liczby[0], liczby[2] = liczby[2], liczby[0]
n = None
m = None
# for i in range(len(liczby)):
# #     if n < liczby[i]:
# #         n = liczby[i]
# #         indeks = i
# #     liczba_max = n
# #     if m > liczby[i]:
# #         m = liczby[i]
# #         indeks = i
# #     liczba_min = m
# #
# #
# #
# # print(f"libczba max:{liczba_max} indeks {indeks}")
# # print(f"libczba max:{liczba_min} indeks {indeks}")


indeks_min, indeks_max = None, None

for indeks in range(len(liczby)):
    if indeks_min is None or liczby[indeks] < liczby[indeks_min]:
        indeks_min = indeks
    if indeks_max is None or liczby[indeks] > liczby[indeks_max]:
        indeks_max = indeks

liczby[indeks_min], liczby[indeks_max] = liczby[indeks_max], liczby[indeks_min]

assert liczby == [1, 2, 5, 4, 3]
