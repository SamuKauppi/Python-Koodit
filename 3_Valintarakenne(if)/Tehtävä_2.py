hyttiLuokka = input("Syötä hyttiluokkasi: ")
hyttiLuokka = hyttiLuokka.lower();
if hyttiLuokka == "lux":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiLuokka == "a":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiLuokka == "b":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiLuokka == "c":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")