import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        for name, info in contacts.items():
            print(f"{name} - Phone: {info['phone']}, Email: {info['email']}")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: {name} - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact {name}")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
