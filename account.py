def printMenu():
    print("[1]. Create Acoount.")
    print("[2]. Exit.")



def inputNewAccountData():
    first = input("First name : ")
    last = input("Last name : ")
    email = input("Email : ")
    username = input("User name : ")
    password = input("Password : ")
    
    data = {
        "firstName":first,
        "lastName":last,
        "email":email,
        "userName":username,
        "password":password }   

    return data

def CreateAccount(userData):
    datastr = userData["firstName"] + "," + userData["lastName"] + "," + userData["email"] + "," + userData["userName"] + "," + userData["password"] + ',' + '0'
    with open("accounts.txt", "a") as file:
        file.write(datastr + "\n")

def main():
    printMenu()
    option = int(input())

    if option == 1: 
        uData = inputNewAccountData()
        print(uData)
        CreateAccount(uData)

    print ("Thank You")


main()