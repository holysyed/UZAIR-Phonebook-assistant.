import json

# Load contacts from file
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number

        # Save to file
        with open("contacts.json", "w") as file:
            json.dump(contacts, file)

        print("Contact saved!")

    elif choice == "2":
        name = input("Enter name: ")
        if name in contacts:
            print("Number:", contacts[name])
        else:
            print("Not found may be added in YOUR cerebal cortex ")

    elif choice == "3":
        print("Goodbye from Uzair ;) ")
        break

    else:
        print("Invalid choice, Are you DUMB? ")