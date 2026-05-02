from searchAccount import searchAccountByUsername
from createAccount import createAccount
from dataManipulation import deposit
from dataManipulation import withdraw


def printMenu():
    print("WELCOME TO THE CENTRAL BANK !")
    
    print("[1]. Create Acoount.")
    print("[2]. Search.")
    print("[3]. Deposit.")
    print("[4]. Withdraw.")
    print("[5]. Exit.")



def main():
    printMenu()
    option = int(input())

    if option == 1: 
        createAccount()

    elif option == 2 :
        searchAccountByUsername()

    elif option == 3 :
        deposit()


    elif option == 4 :
        withdraw()


    elif option == 5 :
        print("Exited Successfully :)")

    print("Thank You !")


main()