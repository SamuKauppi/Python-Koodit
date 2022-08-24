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

# Keksin myöhemmin paremman tavan tehdä tämän
# kolmiKoodi = ""
# neliKoodi = ""
#
# for x in range(3):
#     kolmiKoodi += str(random.randint(0, 9))
# for x in range(4):
#     neliKoodi += str(random.randint(1, 6))
# print("Kolminumeroinen koodi: " + kolmiKoodi)
# print("Nelinumeroinen koodi: " + neliKoodi)