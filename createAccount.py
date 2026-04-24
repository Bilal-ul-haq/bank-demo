from dataManipulation import insertNewAccount

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





def createAccount():
    uData = inputNewAccountData()
    insertNewAccount(uData)        