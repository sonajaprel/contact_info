📒 Contact Book CLI App

A simple Command-Line Contact Book Application built using Python.
This app allows you to add, view, search, and delete contacts, with optional JSON file storage so that contacts are saved between runs.

🚀 Features

Add new contacts (Name, Phone, Email)

View all saved contacts

Search for a contact by name

Delete an existing contact

Automatically saves contacts to a JSON file (contacts.json)

🛠️ Tech Stack

Language: Python 3

IDE: VS Code (or any Python IDE)

Modules:

json → for saving and loading contacts

os → for file handling

📂 Project Structure
contact-book-cli/
│── contacts.json        # Stores saved contacts
│── contact_book.py      # Main Python script
│── README.md            # Project documentation

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/contact-book-cli.git
cd contact-book-cli


Run the script:

python contact_book.py


Use the menu options:

--- Contact Book ---
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit

📸 Sample Output
--- Contact Book ---
1. Add Contact
2. View Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter choice: 1
Enter name: John Doe
Enter phone: 9876543210
Enter email: john@example.com
Contact John Doe added!

📚 Key Concepts Practiced

Dictionaries for storing contacts

Functions for modular code

Loops & Conditionals for user interaction

File Handling with JSON for persistent storage

CLI Interaction using input()
