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


autot = []
for i in range(10):
    bil = Auto(f"ABC-{i + 1}", random.randint(100, 200))
    autot.append(bil)

has_won = False
while not has_won:
    for i in autot:
        i.kiihdyta(random.randint(-10, 15))
        i.kulje(1)
        if i.matka >= 10000:
            has_won = True

autot.sort()
print("---------------")
for i in autot:
    print(f"Rekisterinumero: {i.rekisteri}")
    print(f"Huippunopeus: {i.huippunopeus}")
    print(f"Nykyinen nopeus: {i.nopeus}")
    print(f"Kuljettu matka: {i.matka}")
    print("---------------")
