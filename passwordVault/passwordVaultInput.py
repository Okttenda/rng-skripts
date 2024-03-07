import sysx
import json

passwords = []
max_password = 0

def Password():
  newPassword = input("Gebe ein Passwort ein um es der Liste hinzu zu fügen: ")
  if newPassword == "safe":
    safe_accept()
  else:
    passwords.append(newPassword)
    print("Das Passwort:", newPassword, "wurde erfolgreich der Liste hinzugefügt!")
    max_password =+ 1
    Password()
  

def safe_accept():
    safe_accept = input("Ist das deine Finale eingabe? Deuine alten eingegebenen Passwörter werden gelöscht.\n Bist du dir sicher?: ", "\n (y/n)")
    if safe_accept == "y":
      jsonDump()
      sys.exit()
    elif safe_accept == "n":
      sys.exit()
    else:
      print("Dies ist keine eingabe!")
      safe_accept()


def jsonDump():
  with open("passwordVault.json", "w") as f:
    json.dump(passwords, f)
  with open("passwordVaultMax.json", "w") as f:
    json.dump(max_password, f)

Password()
