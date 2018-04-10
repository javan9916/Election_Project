provinces = []

def addProvince():
    pname = input("Province name: ")
    pdiputies = input("Number of diputies: ")
    province = {"name": pname, "diputies": pdiputies, "cantons": []}
    provinces.append(province)

    return True


def addCanton():
    cname = input("Canton name: ")
    prov = input("This canton belongs to the province of: ")
    f = False
    i = 0
    while i < len(provinces):
        if provinces[i]["name"] == prov:
            canton = {"name": cname, "province": prov, "districts":[]}
            provinces[i]["cantons"].append(canton)
            f = True
            break
        else:
            i += 1

    if f == False:
        print("That province does not exist, check it out\n")

    return True

def addDistrict():
    dname = input("District name: ")
    prov = input("This district belong to the province of: ")
    canton = input("This district belongs to the canton of: ")
    f1 = False
    f2 = False
    j = 0
    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            f2 = True
            while j < len(cantons):
                if cantons[j]["name"] == canton:
                    district = {"name": dname, "province": prov,"canton": canton}
                    cantons[j]["districts"].append(district)
                    f1 = True
                    break
                else:
                    j += 1

    if f1 and f2 == False:
        print("That province or canton does not exist, check'em out\n")
    elif f1 == False:
        print("That canton does not exist, check it out\n")

    return True

def editProvince():
    province = input("Province: ")
    f = False
    i = 0
    while i < len(provinces):
        if provinces[i]["name"] == province:
            provinces[i]["name"] = input("New province name: ")
            provinces[i]["diputies"] = input("New number of deputies: ")
            f = True
        i += 1
        break
    if f == False:
        print("That province does not exist, check it out")

    return True

def editCanton():
    canton = input("Canton: ")
    prov = input("This canton belongs to the province of: ")
    f1 = False
    f2 = False
    i = 0
    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            f2 = True
            while i < len(cantons):
                if cantons[i]["name"] == canton:
                    cantons[i]["name"] = input("New province name: ")
                    f1 = True
                    break
                else:
                    i += 1

    if f1 and f2 == False:
        print("That province or canton does not exist, check'em out\n")
    elif f1 == False:
        print("That canton does not exist, check it out\n")

    return True

def editDistrict():
    district = input("District: ")
    prov =  input("This district belongs to the province of: ")
    canton = input("This district belongs to the canton of: ")
    f1 = False
    f2 = False
    f3 = False
    i = 0
    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            f3 = True
            for c in cantons:
                if c["name"] == canton:
                    districts = c["districts"]
                    f2 = True
                    while i < len(districts):
                        if districts[i]["name"] == district:
                            districts[i]["name"] = input("New district name: ")
                            f1 = True
                            break
                        else:
                            i += 1

    if f1 and f2 and f3 == False:
        print("That province, canton or district does not exist, check'em out\n")
    elif f1 and f2 == False:
        print("That canton or district does not exist, check'em out\n")
    elif f1 == False:
        print("That district does not exist, check it out\n")

    return True

def deleteProvince():
    province = input("Name of province to be deleted: ")
    f = False
    i = 0
    while i < len(provinces):
        if provinces[i]["name"] == province:
            provinces.remove(provinces[i])
            print("Deleted successfully")
            f = True
        break
    if f == False:
        print("That province does not exist, check it out")

    return True

def deleteCanton():
    canton = input("Name of canton to be deleted: ")
    prov = input("This canton belongs to the province of: ")
    f1 = False
    f2 = False
    i = 0
    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            f2 = True
            while i < len(cantons):
                if cantons[i]["name"] == canton:
                    cantons.remove(cantons[i])
                    f1 = True
                    break
                else:
                    i += 1

    if f1 and f2 == False:
        print("That province or canton does not exist, check'em out\n")
    elif f1 == False:
        print("That canton does not exist, check it out\n")

    return True

def deleteDistrict():
    district = input("Name of district to be deleted: ")
    prov = input("This district belongs to the province of: ")
    canton = input("This district belongs to the canton of: ")
    f1 = False
    f2 = False
    f3 = False
    i = 0
    for p in provinces:
        if p["name"] == prov:
            cantons = p["cantons"]
            f3 = True
            for c in cantons:
                if c["name"] == canton:
                    districts = c["districts"]
                    f2 = True
                    while i < len(districts):
                        if districts[i]["name"] == district:
                            districts.remove(districts[i])
                            f1 = True
                            break
                        else:
                            i += 1

    if f1 and f2 and f3 == False:
        print("That province, canton or district does not exist, check'em out\n")
    elif f1 and f2 == False:
        print("That canton or district does not exist, check'em out\n")
    elif f1 == False:
        print("That district does not exist, check it out\n")

    return True


