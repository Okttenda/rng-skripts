import json
import string
filename = "json/Contact_Book.json"
error001 = "[ERROR:001]This Feature is in Progress"
error002 = "[ERROR:002]This was not an option"


def idGenerator():

    id = ""


def showContact():
    with open(filename, "r") as file:
        data = json.load(file)
    print(data)


def addContact():
    with open(filename, "r") as file:
        data = json.load(file)
    entry1 = input("welcher Kontakt: ")
    entry = { "name":entry1 }

    data.append(entry)
    with open(filename, "w") as file:
        json.dump(data, indent=4, sort_keys=True)


def delContact():
    print(error001)


def searchContact():
    print(error001)


print(
    "Wilkommen in deinem Kontaktbuch, was möchtest du tun?\n [1|alle Kontakte zeigen] [2|Kontakt hinzufügen]\n ["
    "3|Kontakt entfernen] [4|Kontakt suchen]")
choice = int(input(""))

if choice == 1:
    showContact()
elif choice == 2:
    print("addContacts")
    addContact()
elif choice == 3:
    delContact()
elif choice == 4:
    searchContact()
elif choice == 5:
    idGenerator()
else:
    print(error002)
