from searchAccount import searchAccountByUsername
from createAccount import createAccount
from deposit import deposit

def printMenu():
    print("WELCOME TO THE CENTRAL BANK !")
    
    print("[1]. Create Acoount.")
    print("[2]. Search.")
    print("[3]. Deposit.")
    print("[4]. Exist.")



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
        print("Exited Successfully :)")

    print("Thank You !")


main()