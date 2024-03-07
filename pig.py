import sys
import time

error001 = "[ERROR001]This is, for the Time being not implementet!"
error002 = "[ERROR002]This was not an Option!"
def player_turn(player):
  print("Spieler:", player, "ist am Zug!")
  print("Was möchtest du tun?")
  print("[Roll Dice | add Score to Total Score | Check Total Score | Exit Game]")
  choice = input(": ")
  try:
    result = int(choice)
    print("int", result)
    if result == 4:
      print("Have a great Day!")
      time.sleep(2)
      sys.exit()
    else:
      print(error002)
      player_turn(player)
  except:
    print("Something went wrong")
    if choice == "Roll Dice":
      print(error001)
    elif choice == "add Score to Total Score":
      print(error001)
    elif choice == "Check Total Score":
      print(error001)
    elif choice == "Exit Game":
      print("Have a great Day!")
      time.sleep(2)
      sys.exit()
    else:
      print(error002)
      player_turn(player)


player_turn(1)
