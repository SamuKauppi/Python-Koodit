class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus=0, matka=0):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
        return


abc_bil = Auto("ABC-123", "142")
print(f"Auton rekisterinumero: {abc_bil.rekisteri}")
print(f"Auton huippunopeus: {abc_bil.huippunopeus}km/h")

