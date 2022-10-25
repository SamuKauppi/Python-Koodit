import random


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

    def kulje(self, tuntimaara):
        self.matka += self.nopeus * tuntimaara
        return

    def __lt__(self, other):
        return self.matka > other.matka


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus = pituus_km
        self.autot = autot
        pass

    def tunti_kuluu(self):
        for a in self.autot:
            a.kiihdyta(random.randint(-10, 15))
            a.kulje(1)
        return

    def tulosta_tilanne(self):
        for a in self.autot:
            print(f"Rekisterinumero: {a.rekisteri}")
            print(f"Huippunopeus: {a.huippunopeus}")
            print(f"Nykyinen nopeus: {a.nopeus}")
            print(f"Kuljettu matka: {a.matka}")
            print("---------------")
        return

    def kilpailu_ohi(self):
        for a in self.autot:
            if a.matka >= 10000:
                print(f"Voittaja on: {a.rekisteri}")
                self.autot.sort()
                return True
        return False


autot = []
for i in range(10):
    bil = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot.append(bil)

spel = Kilpailu("Suuri Romuralli", 8000, autot)
aika = 0
print("Lähtötilanne:")
spel.tulosta_tilanne()
print("")
print("")
while not spel.kilpailu_ohi():
    aika += 1
    spel.tunti_kuluu()
    if aika % 10 == 0:
        spel.tulosta_tilanne()

spel.tulosta_tilanne()
print(f"Kilpailun aika: {aika}")
