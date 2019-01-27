class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def najstarszy(*args):
    dog_ages = []
    for i in args:
        dog_ages.append([i.age,i])
    dog_ages.sort()
    return dog_ages[-1][1]


rex = Dog("Rex", 10)
burek = Dog("Burek", 5)
azor = Dog("Azor", 7)

x = najstarszy(rex, burek, azor) #zwraca instancje - obiekt
print(x.name) #zwraca nazwe instancji

