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
    db.collection("default").add(data)
    print("Data created")


def read():
    print("Read data")
    default = db.collection("default").get()
    for user in default:
        print(user.id, user.to_dict())


def update():
    print("Update data")
    name = input("Name: ")
    age = input("Age: ")
    data = {
        "name": name,
        "age": age
    }
    db.collection("default").document(name).set(data, merge=True)
    print("Data updated")


def delete():
    print("Delete data")
    default = db.collection("default").get()
    for user in default:
        print(user.id, user.to_dict())

    name_to_delete = input("Name: ")
    # Query the collection for documents where the 'name' field matches the input
    matching_docs = db.collection("default").where(
        'name', '==', name_to_delete).get()

    if matching_docs:
        for doc in matching_docs:
            # Delete the document using its document ID
            db.collection("default").document(doc.id).delete()
            print(f"Document with ID {doc.id} deleted")
    else:
        print("No matching document found with the name provided")


def main():
    while True:
        print("Crud python with Firebase")
        print("1. Create data")
        print("2. Read data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")

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
        elif option == "5":
            exit()
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
