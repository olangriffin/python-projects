import programs

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
    print()
    print(f"Hello {name}")
    print()

def choice():
    print("Which program would you like to run?")
    print("Porgram A")
    print("Program B")
    print("Program C")
    print("program D")
    print()
    x = input("choose: ")

    if x == "a" :
        print("You chose program A")
        programs.program_A()
        
    elif x == "b" :
        print("You chose program B")
        programs.program_B()
        
    elif x == "c" :
        print("You chose program C")
        programs.program_C()
        
    elif x == "d" :
        print("You chose program D")
        programs.program_D()
        
    else:
        print("incorrect input. try again")
        choice()

greeting()
choice()
