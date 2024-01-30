from firebase_admin import firestore, credentials
import os
import firebase_admin

# Path to your Firebase project's service account key JSON file
cred_path = 'path/serviceAuth.json'

# Initialize the Firebase SDK
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()


def create():
    print("Create data")
    name = input("Name: ")
    age = input("Age: ")
    data = {
        "name": name,
        "age": age
    }
    db.child("users").push(data)
    print("Data created")


def read():
    print("Read data")
    users = db.child("users").get()
    for user in users:
        print(user.id, user.to_dict())


def update():
    print("Update data")
    name = input("Name: ")
    age = input("Age: ")
    data = {
        "name": name,
        "age": age
    }
    db.child("users").update(data)
    print("Data updated")


def delete():
    print("Delete data")
    db.child("users").remove()
    print("Data deleted")


def main():
    print("Crud python with Firebase")
    print("1. Create data")
    print("2. Read data")
    print("3. Update data")
    print("4. Delete data")

    input("Press Enter to continue...")

    option = input("Select an option: ")

    if option == "1":
        create()
    elif option == "2":
        read()
    elif option == "3":
        update()
    elif option == "4":
        delete()
    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
