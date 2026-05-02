def getUserInput():
    username = input("Enter your Username : ").lower()
    amount = int(input("Enter your amount : "))
    values = {
        "username" : username,
        "amount" : amount
    }

    return values
