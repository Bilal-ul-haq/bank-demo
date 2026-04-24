from searchAccount import searchAccountByUsername
from createAccount import createAccount

def printMenu():
    print("WELCOME TO THE CENTRAL BANK !")
    
    print("[1]. Create Acoount.")
    print("[2]. Search.")
    print("[3]. Exist.")



def main():
    printMenu()
    option = int(input())

    if option == 1: 
        createAccount()

    elif option == 2 :
        searchAccountByUsername()

    elif option == 3 :
        print("Exited Successfully :)")

    print("Thank You !")


main()