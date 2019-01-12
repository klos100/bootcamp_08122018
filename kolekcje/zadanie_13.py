print([i / 10 for i in range(0, 11)])

print({(x, x ** 2, x ** 3) for x in range(-10, 10)})

napisy = {"ala ma kota", "kot", "dupa"}

print({x: len(x) for x in napisy})
