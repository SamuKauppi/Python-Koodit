
while True:
    arvo = float(input("Syötä positiivinen luku tuumina: "))
    if arvo < 0:
        print("Loppui")
        break
    else:
        senttiArvo = arvo * 2.54
        print(f"{arvo} tuumaa on {senttiArvo:0.2f} senttiä")

