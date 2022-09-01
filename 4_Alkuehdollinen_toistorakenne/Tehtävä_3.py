pienin = 0
suurin = 0

while True:
    luku = input("Syötä luku: ")
    if luku == "":
        break
    else:
        luku = float(luku)

    if luku < pienin or pienin == 0:
        pienin = luku
    if luku > suurin or suurin == 0:
        suurin = luku

print(f"Suurin luku: {suurin}")
print(f"Pienin luku: {pienin}")