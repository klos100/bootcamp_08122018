print("      ", end="")
for i in range(10):
    print(f"{i:5}", end="")
print()
print()
for i in range(0, 10):
    print(f"{i:5}", end=" ")
    for j in range(0, 10):
        n = i * j

        print(f"{n:5}", sep=" ", end="")
    print()
