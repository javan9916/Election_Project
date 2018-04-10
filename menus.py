from login_signup import *
from TD import *
from PP import *
from AP import *

def menu():
    print("------------------------------------------")
    print("Main Menu\n"
          "1) Log In\n"
          "2) Sign Up\n"
          "3) Exit")

    option = input("Choose an option: ")
    print("------------------------------------------")
    if option == "1":
        logIn()
    elif option == "2":
        signUp()
    elif option == "3":
        return
    else:
        print("Wrong value")
        menu()

def signUp():
    admin = False
    name = input("Type your full name: ")
    age = int(input("Type your age: "))
    email = input("Type your email: ")
    password = input("Type your password: ")
    id = int(input("Type your ID: "))
    yn = input("Are you going to be an Admin?\n"
                "Press Y/y if yes or any key if not: ")
    if yn == "Y" or yn == "y":
        admin = True

    addPerson(name,age,email,password,id,admin)

    menu()

def logIn():
    print("Log In")
    id = int(input("Write your ID: "))
    password = input("Write your Password: ")
    f = False
    i = 0
    while i < len(peopleList):
        if id == peopleList[i]["id"] and password == peopleList[i]["password"]:
            print("Access granted\n")
            f = True
            Admin(peopleList[i])
            break
        else:
            i += 1
    if f == False:
        print("Access denied\n")
        menu()

def Admin(user):
    if user["admin"] == True:
        menuAdmin()
    else:
        print("idk")

def menuAdmin():
    print("------------------------------------------")
    print("Admin Menu\n"
          "1) Territorial Distribution\n"
          "2) Political Parties\n"
          "3) Ballots\n"
          "4) Results and Consultations\n"
          "5) Log Out\n")

    option = input("Choose an option: ")
    print("------------------------------------------")

    if option == "1":
        TDmenu()
    elif option == "2":
        PPmenu()
    elif option == "3":
        APmenu()
    elif option == "4":
        print("RC")
    elif option == "5":
        menu()
    elif option == "6":
        print(provinces)
        menuAdmin()
    else:
        print("Wrong value")
        menuAdmin()

def TDmenu():
    print("Territorial Distribution Menu\n"
          "1) Province\n"
          "2) Canton\n"
          "3) District\n"
          "4) Back\n")

    option = input("Choose an option: ")
    print("------------------------------------------")

    if option == "1":
        province()
    elif option == "2":
        canton()
    elif option == "3":
        district()
    elif option == "4":
        menuAdmin()
    else:
        print("Wrong value")
        TDmenu()

def province():
    print("------------------------------------------")
    print("1) Add\n"
          "2) Edit\n"
          "3) Delete\n")

    option = input("Choose an option: ")
    print("------------------------------------------")

    if option == "1":
        if addProvince():
            TDmenu()
    elif option == "2":
        if editProvince():
            TDmenu()
    elif option == "3":
        if deleteProvince():
            TDmenu()
    else:
        print("Wrong value")
        TDmenu()

def canton():
    print("------------------------------------------")
    print("1) Add\n"
          "2) Edit\n"
          "3) Delete\n")

    option = input("Choose an option: ")
    print("------------------------------------------")

    if option == "1":
        if addCanton():
            TDmenu()
    elif option == "2":
        if editCanton():
            TDmenu()
    elif option == "3":
        if deleteCanton():
            TDmenu()
    else:
        print("Wrong value")
        TDmenu()

def district():
    print("------------------------------------------")
    print("1) Add\n"
          "2) Edit\n"
          "3) Delete\n")

    option = input("Choose an option: ")
    print("------------------------------------------")

    if option == "1":
        if addDistrict():
            TDmenu()
    elif option == "2":
        if editDistrict():
            TDmenu()
    elif option == "3":
        if deleteDistrict():
            TDmenu()
    else:
        print("Wrong value")
        TDmenu()

def PPmenu():
    print("1) Add\n"
          "2) Edit\n"
          "3) Delete\n"
          "4) Back")

    option = input("Choose an option: ")
    print("-----------------------------------------")

    if option == "1":
        if addParty():
            PPmenu()
    elif option == "2":
        if editParty():
            PPmenu()
    elif option == "3":
        if deleteParty():
            PPmenu()
    elif option == "4":
        menuAdmin()
    else:
        print("Wrong value")
        PPmenu()

def APmenu():
    print("1) Add\n"
          "2) Edit\n"
          "3) Delete\n"
          "4) Back")
    option = input("Choose an option: ")
    print("-----------------------------------------")

    if option == "1":
        if addBallot():
            APmenu()
    elif option == "2":
        if editBallot():
            APmenu()
    elif option == "3":
        if deleteBallot():
            APmenu()
    elif option == "4":
        menuAdmin()
    else:
        print("Wrong value")
        APmenu()

menu()


