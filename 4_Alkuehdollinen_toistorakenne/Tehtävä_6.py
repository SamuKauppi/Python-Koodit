import math
import random

pisteidenMaara = float(input("Syötä kuinka monta pistettä käytän piin laskemiseen: "))
osuvatPisteet = 0
i = 1

while i < pisteidenMaara:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if math.sqrt(x**2 + y**2) <= 1:
        osuvatPisteet += 1

    i += 1
pii = 4 * osuvatPisteet /pisteidenMaara
print(f"Piin arvo on suunnilleen: {pii:0.10}")
