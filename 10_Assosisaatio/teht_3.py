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


class Talo:
    def __init__(self, alinkerros, ylinkerros, hissi_lkm):
        self.hissit = [Hissi(alinkerros, ylinkerros)] * hissi_lkm
        return

    def aja_hissia(self, hissin_index, kerros):
        self.hissit[hissin_index].siirry_kerrokseen(kerros)
        return

    def palohalytys(self):
        print("Palohalytyys!")
        for i in self.hissit:
            i.siirry_kerrokseen(0)
        return


aut = Talo(0, 10, 3)
aut.palohalytys()
