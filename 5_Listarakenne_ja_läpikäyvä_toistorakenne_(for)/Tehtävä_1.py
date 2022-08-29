import random

noppienMaara = int(input("Syötä arpakuutioiden lukumäärä: "))

for i in range(noppienMaara):
    print(f"Noppa {i} arvo on {random.randint(1, 6)}")