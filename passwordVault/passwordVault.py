import json

with open("passwordVault.json", "r") as f:
  file = json.load(f)
  data = json.dumps(file)
with open("passwordVaultMax.json", "r") as f:
  file = json.load(f)
  max = json.dumps(file)

list = 0
def script():
  passwd_attempt = input("Gebe dein Passwort ein: ")
    if passwd_attempt == data[list]:
      list =+ 1
      print("Herlichen Glückwunsch du hast das", list, ". Passwort geknackt!")
      print("\n \n \n")
      if list > max or list == max:
        print("Du hast alle Passwörter geknackt!")
        sys.exit()
      else:
        script()
    else:
      print("Schade das war es nicht.")
      script()
      
    
    

