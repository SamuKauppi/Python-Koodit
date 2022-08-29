import math


def PizzanArvo(halkaisijaCm, hinta):
    sade = float(halkaisijaCm / 2)
    pintaAlaM = (math.pi * sade * sade) / 10000
    arvo = pintaAlaM / hinta
    return arvo

pizzat = []

for x in range(2):
    print(f"Anna pizza {x} tiedot!")
    hinta = float(input("Syötä pizzan hinta: "))
    halkaisija = float(input("Syötä pizzan halkaisija: "))
    pizzat.append(PizzanArvo(halkaisija, hinta))

arvokkaimmanId = 0
for x in range(2):
    if pizzat[arvokkaimmanId] < pizzat[x]:
        arvokkaimmanId = x

print(f"Arokkain pizza on indeksin {arvokkaimmanId} pizza")


