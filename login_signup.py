peopleList = []

def addPerson(name,age,email,password,id,admin):
    newPerson = {"name": name, "age": age, "email": email, "password": password, "id": id, "admin": admin}
    peopleList.append(newPerson)

    print(peopleList)