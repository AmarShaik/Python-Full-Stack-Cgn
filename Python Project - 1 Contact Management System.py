def main():
    manager = ContactManager()

    while True:
        print("--- Contact Management ---")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. List Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        ch = input("Enter choice: ")
        if ch == '1':
            manager.add_contact()
        elif ch == '2':
            manager.update_contact()
        elif ch == '3':
            manager.list_contacts()
        elif ch == '4':
            manager.delete_contact()
        elif ch == '5':
            print("--- You have exited ---")
            break
        else:
            print("Invalid choice")


class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    def show(self):
        print(f"Name is {self.name}; Your phone number is {self.phone}; Your mail-id is {self.email}")
class ContactManager():
    def __init__(self):
        self.contacts = []
    def add_contact(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        self.contacts.append(Contact(name, phone, email))
    def list_contacts(self):
        if not self.contacts:
            print("No contacts found")
            return
        number = 1
        for contact in self.contacts:
            print(f"{number})", end=" ")
            contact.show()
            number += 1
    def update_contact(self):
        self.list_contacts()
        choice = int(input("Select number: "))
        count = 1
        for contact in self.contacts:
            if count == choice:
                contact.name = input("New name: ")
                contact.phone = input("New phone: ")
                contact.email = input("New email: ")
                break
            count += 1
    def delete_contact(self):
        self.list_contacts()
        i = input("Enter number to delete: ")
        if i.isdigit() and 0 < int(i) <= len(self.contacts):
            self.contacts.pop(int(i) - 1)
            print("Contact is deleted")
        else:
            print("Invalid input")
if __name__ == "__main__":
    main()
