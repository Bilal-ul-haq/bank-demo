from input1 import getUserInput
from searchAccount import getAccountDataStr
from searchAccount import parseAccountStr
from searchAccount import prepareAccountStr
from searchAccount import isValidUsername, getLineNumberOfUsername


def LineNumUserName():
    values = userInput()    
    id = getLineNumberOfUsername(values[0])
    return id




def insertNewAccount(userDataDictionary):
    datastr = userDataDictionary["firstName"] + "," + userDataDictionary["lastName"] + "," + userDataDictionary["email"] + "," + userDataDictionary["userName"] + "," + userDataDictionary["password"] + ',' + '0'
    with open("accounts.txt", "a") as file:
        file.write(datastr + "\n")

def replaceLineInFile(lineNum, newText):
    # 1. Read all lines into a list
    with open("accounts.txt", "r") as file:
        lines = file.readlines()

    # 2. Check if the line number actually exists to avoid crashing
    if 0 < lineNum <= len(lines):
        # We use lineNum - 1 because Python lists start at 0
        lines[lineNum - 1] = newText + "\n"
        
        # 3. Write everything back to the file
        with open("accounts.txt", "w") as file:
            file.writelines(lines)
        print(f"Line {lineNum} successfully updated!")
    else:
        print("Error: Line number out of range.")

def addBalance():
    username = getUserInput()

    username1 = username["username"]
    
    linenum = getLineNumberOfUsername(username1)
    datastr = getAccountDataStr(linenum)
    parse = parseAccountStr(datastr)
    line = prepareAccountStr(parse)
    parts = line.strip().split(",")
    balance = username["amount"]
    current_balance = parts[5]
    add = int(parts[5]) + balance
    parts[5] = str(add)
    updated_line = ",".join(parts)
    with open("accounts.txt", "r") as f:
        file_lines = f.readlines()

    file_lines[linenum - 1] = updated_line + "\n"


    with open("accounts.txt", "w") as f:
        f.writelines(file_lines)

    print("Your current balance has been successfully updated! :)")

def deposit():
    addBalance()
    




# To use it
# replaceLineInFile(4, "hello")
# Memona,Haq,m@gmail.com,memona,12345,0

    
