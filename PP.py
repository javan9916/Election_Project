partiesList = []

def addParty():
    pName = input("Name of the Political Party: ")
    pYear = input("Year of creation: ")
    pColors = input("Colors of the Political Party: ")
    pIdea = input("Ideological Movement: ")
    politicalParty = {"name": pName, "year": pYear, "colors": pColors, "IM": pIdea}
    partiesList.append(politicalParty)
    print(partiesList)
    return True

def deleteParty():
    party = input("Political Party to be deleted: ")
    f = False
    i = 0
    while i < len(partiesList):
        if partiesList[i]["name"] == party:
            partiesList.remove(partiesList[i])
            print("Deleted successfully")
            f = True
            break
        i += 1
    if f == False:
        print("That Political Party does not exist...")
    print(partiesList)
    return True

def editParty():
    p = input("Political Party Name: ")
    f = False
    i = 0
    while i < len(partiesList):
        if partiesList[i]["name"] == p:
            partiesList[i]["name"] = input("New name: ")
            partiesList[i]["year"] = input("New year of creation: ")
            partiesList[i]["colors"] = input("New colors ")
            partiesList[i]["IM"] = input("New Ideological Movement: ")
            f = True
            break
        else:
            i += 1
    if f == False:
        print("That Political Party does not exist...")
    print(partiesList)
    return True