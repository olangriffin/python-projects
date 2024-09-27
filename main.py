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
