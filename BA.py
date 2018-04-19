from PP import *
from TD import *
ballotListl = []
ballotListp = []

def addBallot():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("Disctrict where you want this ballot: ")
    type = input("Legislative or Presidential?(p/l): ")
    votes = 0
    parties = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "votes": votes}
        parties.append(partySpecs)

    f1 = False
    f2 = False
    f3 = False
    if type == "l":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                f3 = True
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        f2 = True
                        for d in districts:
                            if dis == d["name"]:
                                ballotListl = d["lBallot"]
                                f1 = True
                                if len(ballotListl) == 0:
                                    ballot = {"province": prov, "canton": can, "district": dis, "type": type, "parties": parties}
                                    ballotListl.append(ballot)
                                else:
                                    i = 0
                                    while i < len(ballotListl):
                                        if prov != ballotListl[i]["district"]:
                                            ballot = {"province": prov, "canton": can, "district": dis, "type": type,
                                                      "parties": partiesList, "votes": votes}
                                            ballotListl.append(ballot)
                                        i += 1
    elif type == "p":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                f3 = True
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        f2 = True
                        for d in districts:
                            if dis == d["name"]:
                                ballotListp = d["pBallot"]
                                f1 = True
                                if len(ballotListp) == 0:
                                    ballot = {"province": prov, "canton": can, "district": dis, "type": type, "parties": parties, "votes": votes}
                                    ballotListp.append(ballot)
                                else:
                                    i = 0
                                    while i < len(ballotListp):
                                        if prov != ballotListp[i]["district"]:
                                            ballot = {"province": prov, "canton": can, "district": dis, "type": type,
                                                      "parties": partiesList, "votes": votes}
                                            ballotListp.append(ballot)
                                        i += 1

    if f1 and f2 and f3 == False:
        print("That province, canton or district does not exist, check'em out\n")
    elif f1 and f2 == False:
        print("That canton or district does not exist, check'em out\n")
    elif f1 == False:
        print("That district does not exist, check it out\n")

    print(ballotListl)
    return True

def editBallot():
    prov = input("Province name: ")
    type = input("Legislative or Presidential?(p/l): ")
    f = False

    if type == "l":
        i = 0
        while i < len(ballotListl):
            if ballotListl[i]["province"] == prov:
                newProvince = input("New province: ")
                for b in ballotListl:
                    if newProvince == b["province"]:
                        print("That province already has a ballot... change it")
                        editBallot()
                    else:
                        ballotListl[i]["province"] == newProvince
                        print("Edited Successfully")
                        f = True
                        break
            i += 1

    elif type == "p":
        if type == "l":
            i = 0
            while i < len(ballotListp):
                if ballotListp[i]["province"] == prov:
                    newProvince = input("New province: ")
                    for b in ballotListp:
                        if newProvince == b["province"]:
                            print("That province already has a ballot... change it")
                            editBallot()
                        else:
                            ballotListp[i]["province"] == newProvince
                            print("Edited Successfully")
                            f = True
                            break
                i += 1


    if f == False:
        print("That ballot does not exist")
    return True

def deleteBallot():
    prov = input("Province's ballot to be deleted: ")
    type = input("Legislative or Presidential?(p/l): ")
    f = False

    if type == "l":
        i = 0
        while i < len(ballotListl):
            if ballotListl[i]["province"] == prov:
                ballotListl.remove(ballotListl[i])
                print("Deleted successfully")
                f = True
                break
            i += 1

    elif type == "p":
        i = 0
        while i < len(ballotListp):
            if ballotListp[i]["province"] == prov:
                ballotListp.remove(ballotListp[i])
                print("Deleted successfully")
                f = True
                break
            i += 1

        if f == False:
            print("That ballot does not exist")
        return True
