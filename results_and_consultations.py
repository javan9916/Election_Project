from territorial_distribution import *
from political_parties import *

#This method allows the admin to add a result(votes) into the party of a ballot
def addResult():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District to add votes: ")
    type = input("Legislative or Presidential?(p/l): ")
    party = input("Party name: ")

    f = False
    if type == "l":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                lBallot = d["lBallot"]
                                parties = lBallot[0]["parties"]
                                votes = input("How much votes do you want to add?: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        f = True
                                        break
                                        print("Successfully added")
                                    i += 1
    elif type == "p":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                pBallot = d["pBallot"]
                                parties = pBallot[0]["parties"]
                                votes = input("How much votes do you want to add?: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        f = True
                                        break
                                        print("Successfully added")
                                    i += 1

    if f == False:
        print("Something went wrong...\n")

    return True

#This method allows the admin to edit a result(votes) from a party in a ballot
def editResult():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District name: ")
    party = input("Party name: ")
    type = input("Legislative or Presidential?(p/l): ")

    f = False
    if type == "l":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                lBallot = d["lBallot"]
                                parties = lBallot[0]["parties"]
                                votes = input("New vote quantity: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        f = False
                                        break
                                    else:
                                        print("That party does not exist... Check it out")
                                    i += 1
    elif type == "p":
        for p in provinces:
            if prov == p["name"]:
                cantons = p["cantons"]
                for c in cantons:
                    if can == c["name"]:
                        districts = c["districts"]
                        for d in districts:
                            if dis == d["name"]:
                                pBallot = d["pBallot"]
                                parties = pBallot[0]["parties"]
                                votes = input("New vote quantity: ")
                                i = 0
                                while i < len(parties):
                                    if party == parties[i]["name"]:
                                        parties[i]["votes"] = votes
                                        f = False
                                        break
                                    else:
                                        print("That party does not exist... Check it out")
                                    i += 1

    if f == False:
        print("Something went wrong...")

    return True

#This method counts each party votes of the national results
def countNationalPartyvotes():
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

#This method counts each party votes of the province results
def countProvincePartyvotes(province):
    votes = 0
    partiesVotes = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "totalVotes": votes}
        partiesVotes.append(partySpecs)

    for p in provinces:
        if p["name"] == province:
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

#This method counts each party votes of the canton results
def countCantonPartyvotes(province, canton):
    votes = 0
    partiesVotes = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "totalVotes": votes}
        partiesVotes.append(partySpecs)

    for p in provinces:
        if p["name"] == province:
            cantons = p["cantons"]
            for c in cantons:
                if c["name"] == canton:
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

#This method counts each party votes of the district results
def countDistrictPartyvotes(province, canton, district):
    votes = 0
    partiesVotes = []
    for party in partiesList:
        partySpecs = {"name": party["name"], "totalVotes": votes}
        partiesVotes.append(partySpecs)

    for p in provinces:
        if p["name"] == province:
            cantons = p["cantons"]
            for c in cantons:
                if c["name"] == canton:
                    districts = c["districts"]
                    for d in districts:
                        if d["name"] == district:
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
                    countNationalPartyvotes()

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
                        countProvincePartyvotes(prov)

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
                            countCantonPartyvotes(prov, can)

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
                                countDistrictPartyvotes(prov, can, dis)

    print("Total votes: "+str(totalvotes))
    for party in partiesList:
        percentage = (party["totalVotes"]*100)/totalvotes
        print(party["name"]+": "+str(party["totalVotes"])+", Vote Percentage: "+str(percentage)+"%")

    return True

def calculateDiputies():
    print("This function is unavailable... We're sorry")














