def add_book():
    '''
    Function to add a new book to the library system.
    :return:
    '''
    print("Add a new book")

def view_books():
    print("View all books")

def search_book():
    print("Search for a book")

def update_book():
    print("Update a book")

def delete_book():
    print("Delete a book")

def borrow_book():
    print("Borrow a book")

def return_book():
    print("Return a book")

while True:
    print("""
    Welcome to Library Management System!
    
    Choose the operation you want to perform:
    1. Add a book
    2. View all books
    3. Search for a book
    4. Update a book
    5. Delete a book
    6. Borrow a book
    7. Return a book
    """)

    try:
        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_book()
        elif choice == 4:
            update_book()
        elif choice == 5:
            delete_book()
        elif choice == 6:
            borrow_book()
        elif choice == 7:
            return_book()
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")