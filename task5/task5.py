contacts = []
def add_contact(name, phone):
    contact = {
        'name': name,
        'phone': phone,
    }
    contacts.append(contact)
    print("Contact added successfully!")
def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts):
        print(f"{idx+1}. Name: {contact['name']}, Phone: {contact['phone']}")
def search_contact(query):
    results = [contact for contact in contacts if query.lower() in contact['name'].lower() or query in contact['phone']]
    if not results:
        print("No contacts found.")
        return
    for contact in results:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
def update_contact(name, phone):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = phone
            print("Contact updated successfully!")
            return
    print("Contact not found.")
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print("Contact deleted successfully!")
def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")

            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            search_contact(query)
        elif choice == '4':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number: ")
            update_contact(name, phone)
        elif choice == '5':
            name = input("Enter name of the contact to delete: ")
            delete_contact(name)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
