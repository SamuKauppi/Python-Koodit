import random

kolmiNumeroinenKoodi = [random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
neliNumeroinenKoodi = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

kolmiKoodi = ""
neliKoodi = ""

for n in kolmiNumeroinenKoodi:
    kolmiKoodi += str(n)
for n in neliNumeroinenKoodi:
    neliKoodi += str(n)

print("Kolminumeroinen koodi: " + kolmiKoodi)
print("Nelinumeroinen koodi: " + neliKoodi)