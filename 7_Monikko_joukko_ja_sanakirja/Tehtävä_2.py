nimet = set()
lukumaara = 0
x = True
while x:
    nimi = input("Syötä nimi: ")

    if nimi == "":
        break

    nimet.add(nimi)
    if len(nimet) != lukumaara:
        print("Uusi nimi")
        lukumaara = len(nimet)
    else:
        print("Aiemmin syötetty nimi")

print("Syötetyt nimet: ")
for i in nimet:
    print(i)
