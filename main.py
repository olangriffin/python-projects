title = """ ____            _           _     _   ___  
|  _ \ _ __ ___ (_) ___  ___| |_  / | / _ \ 
| |_) | '__/ _ \| |/ _ \/ __| __| | || | | |
|  __/| | | (_) | |  __/ (__| |_  | || |_| |
|_|   |_|  \___// |\___|\___|\__| |_(_)___/ 
              |__/                          """


print(title)
print()

def greeting():
    name = input("Name: ")
    print(f"Hello {name}")

def choice():
    print("Which program would you like to run?")
    print("A")
    print("B")
    print("C")
    print("D")
    x = input("choose: ")
    if x == "A":
        print("You chose program A")
    elif x == "B":
        print("You chose program B")
    elif x == "C":
        print("You chose program C")
    elif x == "D":
        print("You chose program D")
    else:
        print("incorrect input. try again")
        choice()

greeting()
choice()
