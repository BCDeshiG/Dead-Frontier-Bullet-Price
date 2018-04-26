#Main body of code
def Bullets():
    while True:
        try:
            B=int(input("Please input the amount of bullets in your stack\n"))
        except ValueError:
            print("INVALID INPUT\n")
        else:
            break
    while True:
        try:
            maxB=int(input("Please input the maximum amount of bullets in a stack\n"))
        except ValueError:
            print("INVALID INPUT\n")
        else:
            break
    while True:
        try:
            maxP=int(input("Please input the amount of money you would sell a max stack of bullets for\n"))
        except ValueError:
            print("INVALID INPUT\n")
        else:
            break
    perBP=maxP/maxB
    P=int(perBP*B)
    print("You should sell your stack for $",P, "\n")

#Menu code
import time
def menu():
    C=0
    while C != "2":
        print("This is the Dead Frontier Bullet Price Calculator")
        print("Please choose an option:")
        C=input("\nOPTION 1: Calculate \nOPTION 2: Exit\n")
        if C == "1":
            Bullets()
        elif C == "2":
            print("Thank you for using this program. Goodbye.")
            time.sleep(1)
            exit()
menu()
