contacts = {}

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Exit")
    choice = input("Choice: ")

    if choice == '1':
        name = input("Name: ")
        number = input("Number: ")
        contacts[name] = number
    elif choice == '2':
        name = input("Enter name: ")
        print(contacts.get(name, "Not found"))
    elif choice == '3':
        break