def GalloonaMuunnos(galloonat):
    return galloonat * 3.785411784


x = True
while x:
    syotto = float(input("Syötä bensiinin määrä gallooneina: "))
    if syotto < 0:
        break
    print(f"{int(syotto)} galloonaa bensiiniä on litroina {GalloonaMuunnos(syotto)}")
