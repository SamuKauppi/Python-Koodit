class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
        return


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def Tulosta_tiedot(self):
        print(f"Nimi: {super().nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara}")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def Tulosta_tiedot(self):
        print(f"Nimi: {super().nimi}")
        print(f"Päätoimittaja: {self.paatoimittaja}")


kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.Tulosta_tiedot()
lehti.Tulosta_tiedot()

