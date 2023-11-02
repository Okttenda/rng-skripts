choice = input("Choice: ")

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
counter = 0
list = 0
func = [print("1"), print("2")]
while counter < 2:
    if choice == abc[list]:
        for elem in list:
            func_to_call = func[elem]

    else:
        counter = counter + 1
        list = list + 1