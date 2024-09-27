print("App 1")
print()

def greeting():
    name = input("Name: ")
    print(f"Hello {name}")

def choice():
    x = input("Do you want to continue? (y/n) ")
    if x == "y":
        print("Ok we will continue")
    elif x == "n":
        exit()
    else:
        print("incorrect input. try again")
        choice()

greeting()
choice()
