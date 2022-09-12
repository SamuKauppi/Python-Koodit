nimet = set()
lukumaara = 0
while True:
    nimi = input("Syötä nimi: ")

    if nimi == "":
        break

    nimet.add(nimi)
    if len(nimet) != lukumaara:
        print("Uusi nimi lisätty")
        lukumaara = len(nimet)
    else:
        print("Aiemmin syötetty nimi")

print("Syötetyt nimet: ")
for i in nimet:
    print(i)
