import math

kayttaja = input("Anna nimesi: ")
print("Hauska tutustua " + kayttaja + "!")

ympuranSade_str = input("Anna ympyrän säde ")
ympuranSade = float(ympuranSade_str)

pintaAla = 2 * math.pi * ympuranSade

print(f"Ympyrän pinta-ala on: {pintaAla:0.2f}")
print(f"{'Pii':12s}:{math.pi:10.5f}")
print(f"{'Neperin luku':12s}:{math.e:10.5f}")
