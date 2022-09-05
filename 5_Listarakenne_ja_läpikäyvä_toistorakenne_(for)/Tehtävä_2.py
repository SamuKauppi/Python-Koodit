lista = []
while 0 == 0:
    syote = input("Syötä luku (tyhjä lopettaa): ")
    if syote == "":
        break
    else:
        syote = int(syote)
    lista.append(syote)

lista.sort(reverse=True)
x = 5
if len(lista) < 5:
    x = len(lista)

print("Viisi suurinta: ")
for i in range(x):
    print(lista[i])
