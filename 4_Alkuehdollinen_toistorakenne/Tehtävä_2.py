
arvo = 0;
while arvo >= 0:
    arvo = float(input("Syötä positiivinen luku tuumina: "))
    if(arvo < 0):
        break
    else:
        senttiArvo = arvo * 2.54
        print(f"{arvo} tuumaa on {senttiArvo:0.2f} senttiä")
print("Loppui")
