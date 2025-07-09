contacts = {}

def create_contact():
    name = input("Enter contact name: ").strip().lower()
    if name in contacts:
        print("Contact already exists.")
    else:
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact added.")

def read_contact():
    name = input("Enter name to search: ").strip().lower()
    if name in contacts:
        print(f"{name.title()}: {contacts[name]}")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ").strip().lower()
    if name in contacts:
        new_number = input("Enter new phone number: ")
        contacts[name] = new_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ").strip().lower()
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def show_all_contacts():
    if not contacts:
        print("No contacts saved.")
    else:
        for name, number in contacts.items():
            print(f"{name.title()}: {number}")

while True:
    print("Contact Book Menu:")
    print("1. Create Contact")
    print("2. Read Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Show All Contacts")
    print("6. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        create_contact()
    elif choice == '2':
        read_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        show_all_contacts()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")