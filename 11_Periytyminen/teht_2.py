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


class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, akku_kap):
        super().__init__(rekisteri, huippunopeus)
        self.akku_kap = akku_kap
        self.keskiKulutus = 0

    def kuluta_kwh(self, matka):
        self.keskiKulutus = matka * 0.2


class Polttoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankin_koko):
        super().__init__(rekisteri, huippunopeus)
        self.tankin_koko = tankin_koko
        self.keskiKulutus = tankin_koko

    def kuluta_lkm(self, matka):
        self.keskiKulutus = matka * 6.7 / 100


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus = pituus_km
        self.autot = autot
        pass

    def tunti_kuluu(self):
        for a in self.autot:
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
autot.append(Sahkoauto("ABC-15", 180, 52.5))
autot.append(Polttoauto("ACD-123", 165, 32.3))

autot[0].kiihdyta(50)
autot[1].kiihdyta(50)

kilpailu = Kilpailu("Juttu", 10000, autot)

for i in range(3):
    kilpailu.tunti_kuluu()

autot[0].kuluta_kwh(autot[0].matka)
autot[1].kuluta_lkm(autot[1].matka)

print(f"Sähköauton kulutus: {autot[0].keskiKulutus:0.2f} kwh/km")
print(f"Sähköauton nopeus: {autot[0].nopeus:0.2f} km/h")
print(f"Sähköauton kuljettu matka: {autot[0].matka:0.2f} km")
print("")
print(f"Polttomoottoriauton kulutus: {autot[1].keskiKulutus:0.2f} l/100km")
print(f"Polttomoottoriauton keskinopeus: {autot[1].nopeus:0.2f} km/h")
print(f"Polttomoottoriauton kuljettu matka: {autot[0].matka:0.2f} km")

