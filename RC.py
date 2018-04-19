from TD import *

def addResult():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District to add votes: ")
    party = input("Party name: ")
    votes = input("How much votes: ")
    type = input("Legislative or Presidential: ")

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
                                parties = lBallot["parties"]
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["parties"]:
                                        parties[i]["votes"] = votes
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
                                parties = pBallot["parties"]
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["parties"]:
                                        parties[i]["votes"] = votes
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

