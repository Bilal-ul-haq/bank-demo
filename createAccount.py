from dataManipulation import insertNewAccount
from searchAccount import getLineNumberOfUsername


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
    line =  getLineNumberOfUsername (uData["userName"])

    if line == 0:
        insertNewAccount(uData)

    else:
        print("Could not create account :(. Please choose a different username.")        