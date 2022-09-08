def GalloonaMuunnos(galloonat):
    return galloonat * 3.785411784


while True:
    syotto = float(input("Syötä bensiinin määrä gallooneina: "))
    if syotto < 0:
        break
    print(f"{int(syotto)} galloonaa bensiiniä on litroina {GalloonaMuunnos(syotto)}")
