abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w', 'x', 'y', 'z']
error = "\nERROR: IN PROGRESS\n"
pi = 3.1415926536


def print_form():
    form = ["Flächeninhalt", "Umfang"]
    counter = 0
    list = 0
    while counter < 2:
        print("Für", form[list], "Drücke", abc[list])
        list = list + 1
        counter = counter + 1
    print("\n")


def flaechen():
    form = ["Quadrat", "Rechteck", "Dreieck", "Parrallelogramm", "Trapez", "Kreis", "Kreissektor", "Kreisring"]
    counter = 0
    list = 0
    while counter < 8:
        print("Für", form[list], "Drücke", abc[list])
        list = list + 1
        counter = counter + 1
    choice = input("\nDeine Fläche: ")
    if choice == "a":
        quadrat()
    elif choice == "b":
        rechteck()
    elif choice == "c":
        dreieck()
    elif choice == "d":
        parrallelogramm()
    elif choice == "e":
        trapez()
    elif choice == "f":
        kreis()
    elif choice == "g":
        kreis_sektor()
    elif choice == "h":
        kreis_ring()
    else:
        print("\nDies ist keine Option.\n")
        flaechen()


# def koerper():
#    print_form()
#    choice = input("\nDein Körper: ")


def quadrat():
    print_form()
    choice = input("Wähle deine Operation: ")
    a_non_int = input("Gebe den Wert a ein: ")
    a = int(a_non_int)
    if choice == "a":
        result = a * a
        print("\nDas Ergebnis beträgt:")
        print("A=", result)
    elif choice == "b":
        result = a * 4
        print("\nDas Ergebnis beträgt:")
        print("U=", result)


def rechteck():
    print_form()
    choice = input("Wähle deine Operation: ")
    a_non_int = input("Gebe den Wert a ein: ")
    a = int(a_non_int)
    b_non_int = input("Gebe den Wert b ein: ")
    b = int(b_non_int)
    if choice == "a":
        result = a * b
        print("Das Ergenis beträgt:")
        print("A=", result)
    elif choice == "b":
        result = a * 2 + b * 2
        print("Das Ergenis beträgt:")
        print("U=", result)
    else:
        print("Dies ist keine Option!")
        rechteck()


def dreieck():
    print_form()
    choice = input("Wähle deine Operation: ")
    if choice == "a":
        g_not_int = input("Gebe den Wert g ein: ")
        g = int(g_not_int)
        h_not_int = input("Gebe den Wert h ein: ")
        h = int(h_not_int)
        result = g * h
        print("\nDas Ergebnis beträgt:")
        print("A=", result)
    elif choice == "b":
        a_not_int = input("Gebe die Seite a ein: ")
        a = int(a_not_int)
        b_not_int = input("Gebe die Seite b ein: ")
        b = int(b_not_int)
        c_not_int = input("Gebe die Seite c ein: ")
        c = int(c_not_int)
        result = a + b + c
        print("\nDas Ergebnis beträgt:")
        print("U=", result)
    else:
        print("Dies ist keine option!")
        dreieck()


def parrallelogramm():
    print_form()
    choice = input("Wähle deine Operation: ")
    if choice == "a":
        g_not_int = input("Gebe die Seite g ein: ")
        g = int(g_not_int)
        h_not_int = input("Gebe den Wert h ein: ")
        h = int(h_not_int)
        result = g * h
        print("\nDas Ergebnis beträgt:")
        print("A=", result)
    elif choice == "b":
        a_not_int = input("Gebe den Wert a ein: ")
        a = int(a_not_int)
        b_not_int = input("Gebe den Wert b ein: ")
        b = int(b_not_int)
        result = 2 * a + 2 * b
        print("\nDas Ergebnis beträgt:")
        print("U=", result)
    else:
        print("Dies ist keine option!")
        dreieck()


def trapez():
    print_form()
    choice = input("Wähle deine Operation: ")
    if choice == "a":
        a_not_int = input("Gebe den Wert a ein: ")
        a = int(a_not_int)
        c_not_int = input("Gebe den Wert c ein: ")
        c = int(c_not_int)
        h_not_int = input("Gebe den Wert h ein: ")
        h = int(h_not_int)
        result = a + c / 2 * h
        print("\nDas Ergebnis beträgt:")
        print("A=", result)
    elif choice == "b":
        a_not_int = input("Gebe den Wert a ein: ")
        a = int(a_not_int)
        b_not_int = input("Gebe den Wert b ein: ")
        b = int(b_not_int)
        c_not_int = input("Gebe den Wert c ein: ")
        c = int(c_not_int)
        d_not_int = input("Gebe den Wert d ein: ")
        d = int(d_not_int)
        result = a + b + c + d
        print("\nDas Ergenis beträgt:")
        print("U=", result)
    else:
        print("Dies ist keine option!")
        dreieck()


def kreis():
    print_form()
    choice = input("Wähle deine Operation: ")
    if choice == "a":
        r_not_int = input("Gebe den Wert r ein: ")
        r = int(r_not_int)
        result = r * r * pi
        print("\nDas Ergenis beträgt:")
        print("A=", result)
    elif choice == "b":
        r_not_int = input("Gebe den Wert r ein: ")
        r = int(r_not_int)
        result = 2 * pi * r
        print("\nDas Ergenis beträgt:")
        print("U=", result)
    else:
        print("Dies ist keine option!")
        kreis()


def kreis_sektor():
    form = ["Flächeninhalt", "Kreisbogen"]
    counter = 0
    list = 0
    while counter < 2:
        print("Für", form[list], "Drücke", abc[list])
        list = list + 1
        counter = counter + 1
    print("\n")
    choice = input("Wähle deine Operation: ")
    if choice == "a":
        r_not_int = input("Gebe den Wert r ein: ")
        r = int(r_not_int)
        alpha_not_int = input("Gebe den Wert ""alpha"" ein: ")
        alpha = int(alpha_not_int)
        result = pi * r * 2 * alpha / 360
        print("\nDas Ergebnis beträgt:")
        print("A=", result)
    elif choice == "b":
        r_not_int = input("Gebe den Wert r ein: ")
        r = int(r_not_int)
        alpha_not_int = input("Gebe den Wert ""alpha"" ein: ")
        alpha = int(alpha_not_int)
        result = 2 * pi * r * alpha / 360
        print("\nDas Ergebnis beträgt:")
        print("b=", result)
    else:
        print("Dies ist keine Option!")
        kreis_sektor()


def kreis_ring():
    r1_not_int = input("Gebe den Wert r aus dem inneren Kreis ein: ")
    r1 = int(r1_not_int)
    r2_not_int = input("Gebe den Wert r aus dem äuserem Kreis ein: ")
    r2 = int(r2_not_int)
    result = pi * r2 - pi * r1
    print("\nDas Ergebnis beträgt:")
    print("A=", result)


print("Wähle deine Berechnungskategorie:\n")
kategorien = ["Flächen", "Körper", "Phytagoras"]
counter = 0
list = 0
while counter < 3:
    print("Für", kategorien[list], "Drücke", abc[list])
    list = list + 1
    counter = counter + 1

print("\n")
choice = input("Tippe deine Entscheidung ein: ")
if choice == "a":
    print("Wähle deine Fläche:\n")
    flaechen()
elif choice == "b":
    print("Wähle deinen Körper\n")
#    koerper()
elif choice == "c":
    print("Wähle deine Rechenart:\n")
