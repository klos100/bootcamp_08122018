import os

folder = r"C:\Users\kurs\workspace"

suma = 0
for sciezka, foldery, pliki in os.walk(folder):
    for plik in pliki:
        n = 0
        if plik.endswith(".py"):
            with open(os.path.join(sciezka,plik)) as f:
                for line in f:
                    n += 1
                    suma += 1
    print(f"{plik}\t{n}")

print(f"suma:  {suma}")




#### z os.listdir

def check_dir(path):
    for name in os.listdir(path): # to miejsce gdzie jest plik ze skryptem
        if os.path.isfile(os.path.join(path,name)):
            if name.endswith(".py"):
                print (os.path.join(path,name))
        if os.path.isdir(name):
            print(check_dir(os.path.join(path,name)))

### python glob

import glob

def  check_dir2(folder):
    for filename in glob.glob('**/*.py', recursive=True): ## ** - wchodz w katalogi wszsytkie, *.py - wybieraj pliki py
        print ((os.path.join(folder,filename)))

check_dir2(folder)



