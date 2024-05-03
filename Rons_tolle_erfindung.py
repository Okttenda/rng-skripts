z = "Sag mir eine Zahl🤯: "


def Marius():
    a = input(z)
    choice = any(c.isalpha() for c in a)
    if choice == True:
        print("Das ist keine Zahl!")
        Marius()
    else:
        result = int(a)
        print(a)
        print(choice)
        print(result)
        if result < 5:
            print("Du noob")
        elif result > 10:
            print("Dies stand nicht zur Option!")
            Marius()
        else:
            print("et funkt :D")


Marius()
