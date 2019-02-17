import sys

f_name = None

if len(sys.argv) > 1:
    f_name = sys.argv[1]


try:
    with open(f_name) as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}: {line}", end="")

except FileNotFoundError:
    print("Nie podales nazwy pliku")