from TD import *

def addResult():
    prov = input("Province name: ")
    can = input("Canton name: ")
    dis = input("District to add votes: ")
    votes = input("How much votes: ")

    f1 = False
    f2 = False
    f3 = False
    i = 0



    if f1 and f2 and f3 == False:
        print("That province, canton or district does not exist, check'em out\n")
    elif f1 and f2 == False:
        print("That canton or district does not exist, check'em out\n")
    elif f1 == False:
        print("That district does not exist, check it out\n")

    return True

