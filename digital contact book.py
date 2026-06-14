contacts = {}
# Add 3 contacts
for i in range(3):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
# Search for a contact
search_name = input("\nEnter name to search: ")
if search_name in contacts:
    print("Phone Number:", contacts[search_name])
else:
    print("Contact not found.")
