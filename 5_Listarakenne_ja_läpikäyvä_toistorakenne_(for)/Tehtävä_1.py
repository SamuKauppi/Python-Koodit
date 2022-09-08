import random

noppienMaara = int(input("Syötä arpakuutioiden lukumäärä: "))
summa = 0
for i in range(noppienMaara):
    noppa = random.randint(1, 6)
    summa += noppa
print(f"Noppien summa on {summa}")
