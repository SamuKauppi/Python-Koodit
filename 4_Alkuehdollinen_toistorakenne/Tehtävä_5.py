print("Kirjaudu sisään")
while True:
    kayt = input("Syötä käyttäjätunnus: ")
    sala = input("Syötä salasana: ")

    if kayt.casefold() == "python" and "rules" == sala:
        print("Tervetuloa")
        break
    if i >= 5:
        print("Pääsy evätty")
        break
    i += 1
    print("Väärä käyttäjätunnus tai salasana")