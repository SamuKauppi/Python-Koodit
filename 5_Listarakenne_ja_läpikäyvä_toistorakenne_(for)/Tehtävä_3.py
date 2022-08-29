luku = int(input("Syötä luku: "))
onAlkuluku = True

for x in range(luku):
    if x != 1 and x != luku and x != 0:
        if luku % x == 0:
            onAlkuluku = False
            break

if onAlkuluku:
    print(f"Luku {luku} on alkuluku")
else:
    print(f"Luku {luku} ei on alkuluku")