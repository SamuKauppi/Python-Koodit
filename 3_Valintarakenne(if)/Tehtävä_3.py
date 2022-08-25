sukupuoli = input("Syötä biologinen sukupuolesi(m/n): ")
hemoglobiini_str = input("Syötä hemoglobiiniarvosi (g/l): ")

hemoglobiini = float(hemoglobiini_str.replace("g/l", ""))

if sukupuoli == "m":
    if(hemoglobiini < 134):
        print("Hemoglobiini arvosi on alhainen")
    elif(hemoglobiini > 195):
        print("Hemoglobiini arvosi on korkea")
    else:
        print("Hempblobiini arvosi on normaali")
elif sukupuoli == "n":
    if(hemoglobiini < 117):
        print("Hemoglobiini arvosi on alhainen")
    elif(hemoglobiini > 175):
        print("Hemoglobiini arvosi on korkea")
    else:
        print("Hempblobiini arvosi on normaali")
else:
    print("Syöttämäsi sukupuoli oli virheelinen (syötä m tai n)")