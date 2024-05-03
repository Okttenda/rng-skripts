import json
import os

base_path = None
choice = None
filename = ""
appdata_path = os.getenv('LOCALAPPDATA')
limit = 0


def path(steam_path=None):
    with open(filename, "r") as file:
        data = json.load(file)
    isdir = os.path.isdir(data)
    if isdir == True:
        print(data)
        steam_path = data
        return steam_path

    else:
        print("Dein Steam Pfad wurde noch nicht angegeben ")
        steam_path = input("Bitte Kopiere hier deinen Steam Pfad hinein: ")
        json_object = json.dumps(steam_path)
        with open(filename, "w") as file:
            file.write(json_object)
        path()


def choose_action():
    options = ["2.1", "latest"]
    print("Welche Version möchtest du spielen?\n" + options[0] + "," + options[1])
    result = input("")


path()

