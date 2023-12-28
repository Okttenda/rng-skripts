import json

filename = "Contact_Book.json"
error001 = "[ERROR:001]This Feature is in Progress"
error002 = "[ERROR:002]This was not an option"


def showContact():
    with open(filename, "r") as file:
        data = json.load(file)
    print(data)


def addContact():
    entry = input("welcher Kontakt: ")
    with open(filename, "r") as file:
        data = json.load(file)
    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, file)


def delContact():
    error001


def searchContact():
    error001


print(
    "Wilkommen in deinem Kontaktbuch, was möchtest du tun?\n [1|alle Kontakte zeigen] [2|Kontakt hinzufügen]\n [3|Kontakt entfernen] [4|Kontakt suchen]")
choice = input("")
if choice == 1:
    showContact()
elif choice == 2:
    addContact()
elif choice == 3:
    delContact()
elif choice == 4:
    searchContact()
else:
    error002
