class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nykyinenkerros = self.alinkerros
        return

    def siirry_kerrokseen(self, kerros):
        if self.alinkerros <= kerros <= self.ylinkerros:
            self.nykyinenkerros = kerros
            print(f"Siirryit kerrokseen {self.nykyinenkerros}")
        else:
            print("Valittu kerros on virheellinen")
        return

    def kerros_ylos(self):
        if self.alinkerros <= self.nykyinenkerros < self.ylinkerros:
            self.nykyinenkerros += 1
            print(f"Nousit kerrokseen {self.nykyinenkerros}")
        else:
            print("Olet korkeimmassa kerroksessa ja et voi laskea")
        return

    def kerros_alas(self):
        if self.alinkerros < self.nykyinenkerros <= self.ylinkerros:
            self.nykyinenkerros -= 1
            print(f"Laskit kerrokseen {self.nykyinenkerros}")
        else:
            print("Olet alimassa kerroksessa ja et voi nousta")
        return


h = Hissi(0, 10)
h.kerros_alas()
h.kerros_ylos()
h.siirry_kerrokseen(10)
h.kerros_ylos()
h.kerros_alas()
h.siirry_kerrokseen(0)
h.siirry_kerrokseen(-69)
