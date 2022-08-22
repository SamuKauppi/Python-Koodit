levis = float(input("Syötä leiviskät: "))
naulat = float(input("Syötä naulat: "))
luodit = float(input("Syötä luodit: "))

summa = (((levis * 20) + naulat) * 32 + luodit) * 13.3
kilogrammat = summa/1000
grammat = (kilogrammat - int(kilogrammat)) * 1000
print("Massa nykymittojen mukaan: ")
print(f"{int(kilogrammat)} kilogrammaa ja {grammat:0.2f} grammaa")