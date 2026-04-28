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

def perpareAccountStr(accDictionary):
    string = accDictionary["first_name"] +','+ accDictionary["last_name"] +','+ accDictionary["email"] +','+ accDictionary["username"] +','+ accDictionary["password"] +','+ str(accDictionary["balance"])
    return string 


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
     
     print("########################################")
     print("First Name:", accDictionary["first_name"])
     print("Last Name:", accDictionary["last_name"])
     print("Email:", accDictionary["email"])
     print("Username:", accDictionary["username"])
     print("Password:", accDictionary["password"])
     print("Balance:",accDictionary["balance"])

def searchAccountByUsername():
    userinput = input("Enter Username Please : ").lower()
    accountcount = getAccountNumbers()
    found = False
    for x in range (accountcount):
        accountDataStr = getAccountDataStr(x+1) 
        accountDictionary = parseAccountStr(accountDataStr)
        username = accountDictionary["username"].lower()
        substringIndex = username.find(userinput)
        if substringIndex >= 0:
            printFormattedAccountDictionary(accountDictionary)
            found = True
        
        
    if not found:
        print("no record found")

    
                      
def isValidUsername(searchUsername):

    accountcount = getAccountNumbers()
    found = False
    for x in range (accountcount):
        accountDataStr = getAccountDataStr(x+1) 
        accountDictionary = parseAccountStr(accountDataStr)
        username = accountDictionary["username"].lower()

        if searchUsername.lower() == username :
            found = True
            break
        
        
    return found


def getLineNumberOfUsername(searchUsername):
    accountcount = getAccountNumbers()
    # print(accountcount)
    found = False
    for x in range (accountcount):
        accountDataStr = getAccountDataStr(x+1) 
        # print(accountDataStr)
        accountDictionary = parseAccountStr(accountDataStr)
        # print(accountDictionary)
        username = accountDictionary["username"].lower()
        # print(username)
        if searchUsername.lower() == username:
            return x+1

    return 0


line = getAccountDataStr(4)
d = parseAccountStr(line)
string = perpareAccountStr(d)
print(line)
print(d)
print(string)
