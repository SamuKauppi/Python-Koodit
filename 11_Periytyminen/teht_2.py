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
        self.akku = akku_kap
        self.keskiKulutus = 20 / 100

    def kuluta(self, matka):
        if self.akku > 0:
            self.akku -= matka * self.keskiKulutus
        if self.akku < 0:
            self.akku = 0
            self.nopeus = 0


class Polttoauto(Auto):
    def __init__(self, rekisteri, huippunopeus, tankin_koko):
        super().__init__(rekisteri, huippunopeus)
        self.bensan_maara = tankin_koko
        self.keskiKulutus = 6.9 / 100

    def kuluta(self, matka):
        if self.bensan_maara > 0:
            self.bensan_maara -= matka * self.keskiKulutus
        if self.bensan_maara < 0:
            self.nopeus = 0
            self.bensan_maara = 0


class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus = pituus_km
        self.autot = autot
        pass

    def tunti_kuluu(self):
        for a in self.autot:
            a.kulje(1)
            a.kuluta(a.matka)
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

autot[0].kiihdyta(100)
autot[1].kiihdyta(100)

kilpailu = Kilpailu("Juttu", 10000, autot)

for i in range(3):
    kilpailu.tunti_kuluu()

print(f"Sähköauton kulutus: {autot[0].keskiKulutus * 100:0.2f} kwh/100 km")
print(f"Sähköauton kuljettu matka: {autot[0].matka:0.2f} km")
print(f"Sähköauton jäljellä oleva akku: {autot[0].akku:0.2f} kwh")
print("")
print(f"Polttomoottoriauton kulutus: {autot[1].keskiKulutus * 100:0.2f} l/100 km")
print(f"Polttomoottoriauton kuljettu matka: {autot[1].matka:0.2f} km")
print(f"Polttomoottoriauton jäljellä oleva bensa: {autot[1].bensan_maara:0.2f} l")
