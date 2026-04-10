def parseAccountStr(accountstr):
    data=accountstr.split(",")
   
    return {
        "first_name": data[0],
        "last_name": data[1],
        "email": data[2],
        "username": data[3],
        "password": data[4],
        "balance": int(data[5])
    }

def getAccountDataStr(lineNum):
    with open("accounts.txt", "r") as file:
        lines = file.readlines()
    
    if len(lines) >= lineNum:
        return lines[lineNum-1]
    else:
        return None

def getAccountNumbers():
        with open("accounts.txt", "r") as file:
            lines = file.readlines()

        count = len(lines)
        return count

def printFormattedAccountDictionary(accDictionary):
     print(accDictionary)
     print("########################################")
     print("First Name:", accDictionary["first_name"])
     print("Last Name:", accDictionary["last_name"])
     print("Email:", accDictionary["email"])
     print("Username:", accDictionary["username"])
     print("Password:", accDictionary["password"])
     print("Balance:",accDictionary["balance"])

def searchAccountByUsername():
    userinput = input("Enter Username Please : ")
    accountcount = getAccountNumbers()
    found = False
    for x in range (accountcount):
        accountDataStr = getAccountDataStr(x+1) 
        accountDictionary = parseAccountStr(accountDataStr)
        if accountDictionary["username"] == userinput:
            printFormattedAccountDictionary(accountDictionary)
            found = True
            break

    if not found:
        print("no record found")

# print(parseAccountStr("john,doe,j@gmail.com,johnie,doeie,10"))