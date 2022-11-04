class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.nykyinenkerros = self.alinkerros
        return

    def siirry_kerrokseen(self, kerros):
        if self.alinkerros <= kerros <= self.ylinkerros:
            while kerros != self.nykyinenkerros:
                if kerros < self.nykyinenkerros:
                    self.kerros_alas()
                elif kerros > self.nykyinenkerros:
                    self.kerros_ylos()
                else:
                    break
        else:
            print("Valittu kerros on virheellinen")
        print(f"Saavuit kerrokseen {self.nykyinenkerros}")
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
        for i in range(len(self.hissit)):
            self.aja_hissia(i, self.hissit[i].alinkerros)
        return


aut = Talo(0, 10, 3)
aut.aja_hissia(0, 10)
aut.aja_hissia(1, 5)
aut.aja_hissia(2, 7)
aut.palohalytys()
