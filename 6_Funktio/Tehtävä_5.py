def ParittomatPois(luvut):
    for x in luvut:
        if x % 2 != 0:
            luvut.remove(x)
    return


lukuja = [1, 23, 34, 243, 342, 3123]
print(lukuja)
ParittomatPois(lukuja)
print(lukuja)
