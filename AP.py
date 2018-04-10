from PP import *
ballotList = []

def addBallot():
    ballotName = input("Ballot Name: ")
    print("What type of Ballot it will be?")
    ballotType = input("Type Presidental or Legislative: ")
    ballotPList = partiesList
    ballotSpecs = {"name": ballotName, "type": ballotType, "parties": ballotPList}
    ballotList.append(ballotSpecs)
    return True

def editBallot():
    ballot = input("Ballot name")
    f = False

def deleteBallot():
    ballot = input("Ballot to be deleted: ")
    f = False
    i = 0
    while i < len(ballotList):
        if ballotList[i]["name"] == ballot:
            ballotList.remove(ballotList[i])
            print("Deleted successfully")
            f = True
            break
        i += 1
    if f == False:
        print("That ballot does not exist")
    return True

