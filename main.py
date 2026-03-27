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
        print("Contact saved!")

    elif choice == "2":
        name = input("Enter name: ")
        if name in contacts:
            print("Number:", contacts[name])
        else:
            print("Not found")

    elif choice == "3":
        break

    else:
        print("Invalid choice")