i = "alku";
pienin = 0
suurin = 0

while i != "":
    luku = input("Syötä luku: ")
    if(luku == ""):
        break
    else:
        luku = float(luku)

    if(luku < pienin):
        pienin = luku
    if(luku > suurin):
        suurin = luku

print(f"Suurin luku: {suurin}")
print(f"Pienin luku: {pienin}")