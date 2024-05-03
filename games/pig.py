import sys
import time

error001 = "[ERROR001]This is, for the Time being not implementet!"
error002 = "[ERROR002]This was not an Option!"
error003 = "[ERROR003]Something went Wrong!"


def player_turn(player):
    print("Spieler", player, "ist am Zug!")
    print("Was möchtest du tun?")
    print("[Roll Dice | add Score to Total Score | Check Total Score | Exit Game]")
    choice = input(": ")
    result = 0
    try:
        result = int(choice)
    except:
        result = choice
    finally:
        if result == "Roll Dice" or 1:
            print("bd")
        elif result == "add Score to Total Score" or 2:
            print(error001)
        elif result == "Check Total Score" or 3:
            print(error001)
        elif result == "Exit Game" or 4:
            print("Have a great Day!")
            time.sleep(2)
            sys.exit()
        elif result == 0:
            print(error003)
        else:
            print(error002)
            player_turn(player)


player_turn(1)
