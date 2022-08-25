kalanMitta_str = input("Syötä kuhan pituus senttimetreinä: ")

kalanMitta = float(kalanMitta_str.replace("cm", ""))

if kalanMitta < 37:
    print(f"Kuha on alamittainen. Laske se takaisin järveen. Pituutta puuttuu {37 - kalanMitta:0.1f}cm")
else:
    print("Kuha on sallitun pituinen")