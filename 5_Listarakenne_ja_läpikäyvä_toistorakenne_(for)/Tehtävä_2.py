lista = []
while True:
    syote = input("Syötä luku (tyhjä lopettaa): ")
    if syote == "":
        break
    else:
        syote = int(syote)
    lista.append(syote)

lista.sort(reverse=True)

print("Viisi suurinta: ")
for i in lista[0:5]:
    print(i)
