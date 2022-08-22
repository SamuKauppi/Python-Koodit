kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

print(f"{'Suorakulmion piiri':18s}:{(kanta + korkeus) * 2:10.2f}")
print(f"{'Suorakulmion pinta-ala':18s}:{kanta * korkeus:10.2f}")