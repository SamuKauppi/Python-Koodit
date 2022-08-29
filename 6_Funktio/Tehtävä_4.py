def LukujenSumma(luvut):
    summa = 0
    for x in luvut:
        summa += x
    return summa

lukuja = [1, 23, 34, 243, 342, 3123]
summa = LukujenSumma(lukuja)
print(summa)
