class Auto:
    def __init__(self, rekisteri, huippunopeus, nopeus=0, matka=0):
        self.rekisteri = rekisteri
        self.huippunopeus = int(huippunopeus)
        self.nopeus = nopeus
        self.matka = matka
        return

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus < 0:
            self.nopeus = 0
        elif self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        return


abc_bil = Auto("ABC-123", "142")
print(f"Auton rekisterinumero: {abc_bil.rekisteri}")
print(f"Auton huippunopeus: {abc_bil.huippunopeus}")
abc_bil.kiihdyta(30)
abc_bil.kiihdyta(70)
abc_bil.kiihdyta(50)
abc_bil.kiihdyta(-200)
print(f"Auton nopeus nyt: {abc_bil.nopeus}km/h")
