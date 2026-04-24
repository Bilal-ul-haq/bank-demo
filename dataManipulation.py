def insertNewAccount(userDataDictionary):
    datastr = userDataDictionary["firstName"] + "," + userDataDictionary["lastName"] + "," + userDataDictionary["email"] + "," + userDataDictionary["userName"] + "," + userDataDictionary["password"] + ',' + '0'
    with open("accounts.txt", "a") as file:
        file.write(datastr + "\n")