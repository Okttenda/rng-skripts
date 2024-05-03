import customtkinter
import random
import string

error001 = "[ERROR001]: This is not a Number!"

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()  # create CTk window like you do with the Tk window
root.geometry("400x240")

def get_user_input():
    if input_ch.get() == string:
        characters = int(input_ch.get())
        return characters
    else:
        print(error001)

def function():
    characters = get_user_input()
    printables = string.printable
    i = 0
    password = []
    while i < characters:
        letter = random.choice(printables)
        password.append(letter)
        i += 1
    return password

def button_event():
    t1 = function
    password = "".join(t1)
    print(password)

Label = customtkinter.CTkLabel(root, text="How many Characters should your password have?")
Label.pack(pady=30)
input_ch = customtkinter.CTkEntry(root)
input_ch.pack(pady=20)
button = customtkinter.CTkButton(root, text="Generate", command=button_event)
button.pack(pady=20)

root.mainloop()