from searchAccount import isValidUsername, getLineNumberOfUsername

def getUserInput():
    username = input("Enter your Username : ").lower()
    amount = int(input("Enter your amount : "))
    values = {
        "username" : username,
        "amount" : amount
    }

    return values

def deposit():
    
    values = getUserInput()
    # found = isValidUsername(values["username"])
    # if found :
    #     print("found !")
    # else :
    #     print("not found ")
    
    id = getLineNumberOfUsername(values["username"])
    print(id)