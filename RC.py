from TD import *

#This method allows the admin to add a result(votes) into the party of a ballot
def addResult():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District to add votes: ")
    type = input("Legislative or Presidential?(p/l): ")
    party = input("Party name: ")

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
                                lBallot = d["lBallot"]
                                f1 = True
                                parties = lBallot[0]["parties"]
                                votes = input("How much votes do you want to add?: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        break
                                    else:
                                        print("That party does not exist... Check it out")
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
                                pBallot = d["pBallot"]
                                f1 = True
                                parties = pBallot[0]["parties"]
                                votes = input("How much votes do you want to add?: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        break
                                    else:
                                        print("That party does not exist... Check it out")
                                    i += 1

    if f1 and f2 and f3 == False:
        print("That province, canton or district does not exist, check'em out\n")
    elif f1 and f2 == False:
        print("That canton or district does not exist, check'em out\n")
    elif f1 == False:
        print("That district does not exist, check it out\n")

    return True

#This method allows the admin to edit a result(votes) from a party in a ballot
def editResult():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District name: ")
    party = input("Party name: ")
    type = input("Legislative or Presidential?(p/l): ")

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
                                lBallot = d["lBallot"]
                                f1 = True
                                parties = lBallot[0]["parties"]
                                votes = input("New vote quantity: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        break
                                    else:
                                        print("That party does not exist... Check it out")
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
                                pBallot = d["pBallot"]
                                f1 = True
                                parties = pBallot[0]["parties"]
                                votes = input("New vote quantity: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        break
                                    else:
                                        print("That party does not exist... Check it out")
                                    i += 1

    if f1 and f2 and f3 == False:
        print("That province, canton or district does not exist, check'em out\n")
    elif f1 and f2 == False:
        print("That canton or district does not exist, check'em out\n")
    elif f1 == False:
        print("That district does not exist, check it out\n")

    return True