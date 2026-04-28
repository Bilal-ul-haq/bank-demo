
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

# To use it
replaceLineInFile(4, "hello")
# Memona,Haq,m@gmail.com,memona,12345,0
def addBalance(username, amount):
    
