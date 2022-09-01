import random

satArvo = random.randint(1, 10)
arvaus = 0
print("Arvaa luku 1 - 10 väliltä!")
while arvaus != satArvo:
    arvaus = float(input("Syöttö: "))
    if arvaus > satArvo:
        print("Liian suuri arvaus")
    if arvaus < satArvo:
        print("Liian pieni arvaus")
print("Oikein")