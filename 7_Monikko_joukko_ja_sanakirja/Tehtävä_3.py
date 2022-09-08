def OnkoKirjastossa(kirjasto, avain):
    for i in kirjasto:
        if i == avain:
            return True
    return False


lentoasemat = {}
while True:
    print("\n")
    print("Haluatko lisätä vai hakea lentoasemoja? (add, search, x)")
    komento = input("Syöttö: ")
    if komento == "add":
        icoa = input("Syötä ICOA-koodi: ")
        if OnkoKirjastossa(lentoasemat, icoa):
            print("(Varoitus: Avain on jo käytössä!)")
            if input("Tallennetaanko uusi? (y/n): ") != "y":
                continue

        nimi = input("Syötä lentoaseman nimi: ")
        lentoasemat.update({icoa: nimi})
        print("Lentoasema lisätty")

    elif komento == "search":
        icoa = input("Syötä ICOA-koodi: ")
        if OnkoKirjastossa(lentoasemat, icoa):
            print(f"Icoa-koodi:{icoa} vastaa lentoasemaa: {lentoasemat.get(icoa)}")
        else:
            print("Lentoasemaa ei löytynyt")

    elif komento == "x":
        print("Poistutaan ohjelmasta...")
        break
    else:
        print("Väärä komento")
