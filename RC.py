from TD import *
from PP import *

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
                                        print("Successfully added")
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
                                        print("Successfully added")
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

#This method counts each party votes
def countPartyvotes():
    votes = 0
    partiesVotes = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "totalVotes": votes}
        partiesVotes.append(partySpecs)

    for p in provinces:
        cantons = p["cantons"]
        for c in cantons:
            districts = c["districts"]
            for d in districts:
                ballot = d["pBallot"]
                parties = ballot[0]["parties"]
                i = 0
                while i < len(parties):
                    if partiesVotes[i]["name"] == parties[i]["name"]:
                        partiesVotes[i]["totalVotes"] += int(parties[i]["votes"])
                    i += 1

    i = 0
    while i < len(partiesList):
        if partiesList[i]["name"] == partiesVotes[i]["name"]:
            partiesList[i]["totalVotes"] = partiesVotes[i]["totalVotes"]
        i += 1

#This method calculates the total votes and the percentage nationally
def nationalResults():
    totalvotes = 0

    for p in provinces:
        cantons = p["cantons"]
        for c in cantons:
            districts = c["districts"]
            for d in districts:
                ballot = d["pBallot"]
                parties = ballot[0]["parties"]
                for prts in parties:
                    totalvotes += int(prts["votes"])
                    countPartyvotes()

    print("Total votes: "+str(totalvotes))
    for party in partiesList:
        percentage = (party["totalVotes"]*100)/totalvotes
        print(party["name"]+": "+str(party["totalVotes"])+", Vote Percentage: "+str(percentage)+"%")

    return True

#This method calculates the total votes and the percentage provincially
def provinceResults():
    prov = input("Province name: ")
    totalvotes = 0

    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            for c in cantons:
                districts = c["districts"]
                for d in districts:
                    ballot = d["pBallot"]
                    parties = ballot[0]["parties"]
                    for prts in parties:
                        totalvotes += int(prts["votes"])
                        countPartyvotes()

    print("Total votes: "+str(totalvotes))
    for party in partiesList:
        percentage = (party["totalVotes"]*100)/totalvotes
        print(party["name"]+": "+str(party["totalVotes"])+", Vote Percentage: "+str(percentage)+"%")

    return True

#This method calculates the total votes and the percentage cantonally
def cantonResults():
    prov = input("Province name: ")
    can = input("Canton name: ")
    totalvotes = 0

    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            for c in cantons:
                if c["name"] == can:
                    districts = c["districts"]
                    for d in districts:
                        ballot = d["pBallot"]
                        parties = ballot[0]["parties"]
                        for prts in parties:
                            totalvotes += int(prts["votes"])
                            countPartyvotes()

    print("Total votes: "+str(totalvotes))
    for party in partiesList:
        percentage = (party["totalVotes"]*100)/totalvotes
        print(party["name"]+": "+str(party["totalVotes"])+", Vote Percentage: "+str(percentage)+"%")

    return True

#This method calculates the total votes and the percentage districtally
def districtResults():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District name: ")
    totalvotes = 0

    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            for c in cantons:
                if c["name"] == can:
                    districts = c["districts"]
                    for d in districts:
                        if d["name"] == dis:
                            ballot = d["pBallot"]
                            parties = ballot[0]["parties"]
                            for prts in parties:
                                totalvotes += int(prts["votes"])
                                countPartyvotes()

    print("Total votes: "+str(totalvotes))
    for party in partiesList:
        percentage = (party["totalVotes"]*100)/totalvotes
        print(party["name"]+": "+str(party["totalVotes"])+", Vote Percentage: "+str(percentage)+"%")

    return True

#This method calculates the number of diputies that correspond in each province
"""def calculateDiputies():
    diputies = 0
    totalvotes = 0
    quotient = 0
    partyDiputies = 0
    lowPriority = []
    highPriority = []
    provinceDiputies = []
    for p in provinces:
        provinceSpecs = {"name": p["name"], "diputies": p["diputies"], "quotient": quotient, "partyDiputies": partyDiputies, "totalVotes": totalvotes}
        provinceDiputies.append(provinceSpecs)

    for p in provinces:
        cantons = p["cantons"]
        for c in cantons:
            districts = c["districts"]
            for d in districts:
                ballot = d["lBallot"]
                parties = ballot[0]["parties"]
                i = 0
                while i < len(parties):
                    if provinceDiputies[i]["name"] == parties[i]["name"]:
                        provinceDiputies[i]["totalVotes"] += int(parties[i]["votes"])
                    i += 1

    i = 0
    while i < len(provinceDiputies):
        provinceDiputies[i]["quotient"] = provinceDiputies[i]["totalVotes"]/provinceDiputies[i]["diputies"]
        if partiesList[i]["totalVotes"] < provinceDiputies[i]["quotient"]:
            lowPriority.append(provinceDiputies[i])
        else:
            highPriority.append(provinceDiputies[i])
        i += 1

    i = 0
    while i < len(highPriority):
        while diputies <= highPriority[i]["diputies"]:
            while highPriority[i]["quotient"] < highPriority[i]["totalVotes"]:
                highPriority[i]["totalVotes"] -= highPriority[i]["quotient"]
                provinceDiputies[i]["partyDiputies"] += 1
                diputies += 1"""





