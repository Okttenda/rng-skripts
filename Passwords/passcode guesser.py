import random

debug001 = "Schleife Ausgeführt!\n"


def generator():
    counter = 0
    print("test")
    while counter < 4:
        print(debug001)
        rng = random.randint(0, 1)

        counter = counter + 1


generator()