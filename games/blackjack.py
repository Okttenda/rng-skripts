import random
import json
import os
import sys
import time

defaultJSONDict = {
"player0": "2000",
"player1": "2000",
"player2": "2000",
"player3": "2000"
}
defaultJSON = json.dumps(defaultJSONDict, indent=4)



error001 = "ERROR[001]:This was not an option you dumbass!"

def mainMenu():
    print("Wilkommen bei Blackjack!")
    inp = input("[ Start | Exit | Reset Money ]")
    if inp == "Exit":
        print("Tschüss!")
        time.sleep(4)
        sys.exit()
    elif inp == "Start":
        players = input("Wie viele Spieler spielen mit? \n max. 4 Spieler")
        print("\n \n")
    elif inp == "Reset Money":
        with open("money.json", "w") as f:
            f.write(defaultJSON)
            f.close()
        print("\n \n \n \n \n \n")
        main()
    else:
        print(error001)
        print("\n \n \n \n \n \n")
        main()
    return players

def Zug(players):
    playersInt = int(players)
    i = 0
    while i < playersInt:
        print(i)
        currentPlayer = str(i + 1)
        print("Spieler " + currentPlayer + ", Was möchtest du tun?")
        print("[ Hit | Pass ]")
        inp = input()
        # put card calc function
        if inp == "Hit":
            pass
        elif inp == "Pass":
            pass
        else:
            print(error001)
        i = i + 1
    
    zug = input("Spieler  was möchtest du tun?")

def cardCalc():
    card1 = random.randrange(2, 13)
    list = [10, 12, 13]
    if card1 == list:
        print("Wert = 10")
    else:
        print("Wert =" + card1)


def extract_json(json_data, key):
    data = json.loads(json_data)
    value = data.get(key)
    return value

def loadMoney():
    isExisting = os.path.exists("money.json")
    if isExisting == False:
        with open("money.json", "w") as f:
            f.write(defaultJSON)
            f.close()
            loadMoney()
    else:
        with open("money.json", "r") as f:
            file = json.load(f)
            data = json.dumps(file)
        player0 = extract_json(data, "player0")
        player1 = extract_json(data, "player1")
        player2 = extract_json(data, "player2")
        player3 = extract_json(data, "player3")
    return player0, player1, player2, player3
    

def main():
    playerCount = mainMenu()
    Zug(playerCount)



if __name__ == "__main__":
    main()