import random


def NopanHeitto():
    return random.randint(1, 6)


i = 0
while i != 6:
    i = NopanHeitto()
    print(i)
