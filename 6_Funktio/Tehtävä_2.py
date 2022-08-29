import random


def NopanHeitto(tahkojenMaara):
    return random.randint(1, tahkojenMaara)


i = 0
tahkojenMaara = int(input("Syötä nopan tahkojen määrä: "))
while i != tahkojenMaara:
    i = NopanHeitto(tahkojenMaara)
    print(i)
