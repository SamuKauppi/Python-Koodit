luku = int(input("Syötä luku: "))
onAlkuluku = True

for x in range(1, luku):
    if luku % x == 0:
        onAlkuluku = False
        break

if onAlkuluku:
    print(f"Luku {luku} on alkuluku")
else:
    print(f"Luku {luku} ei on alkuluku")
