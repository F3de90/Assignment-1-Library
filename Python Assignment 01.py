# Simple Library Management System
# Developed for The Great Hartland Community Library
# Author: Federico Mossa
# Student Number: 2314622

# List to store all book records, each as a dictionary
library_books = []

# Function to display the main menu
def main_menu():
    print("\n--- Welcome to Great Hartland Library System ---")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. Display All Books")
    print("4. Check Out a Book")
    print("5. Check In a Book")
    print("6. Exit")

# Function to add a new book
def add_book():
    print("\n--- Add a New Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()  # Unique identifier
        # Check for duplicate ID before adding
        for book in library_books:
            if book['id'] == book_id:
                print("A book with this ID already exists.")  # Error message for duplicate
                return

        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()
        year = input("Enter Year of Publication: ").strip()

        if not year.isdigit():
            raise ValueError("Year must be a number.")  # Custom error for non-numeric year input

        # Create a new book entry using a dictionary
        book = {
            'id': book_id,
            'title': title,
            'author': author,
            'year': int(year),
            'available': True  # Default to available
        }

        library_books.append(book)  # Add book to library
        print("Book added successfully!")

    except ValueError as ve:
        print(f"Error: {ve}")  # Display specific validation error (For example: year not numeric)
    except Exception as e:
        print(f"Unexpected error: {e}")  # Catch-all for any other unexpected issues

# Function to search for a book by title or author
def search_book():
    print("\n--- Search for a Book ---")
    try:
        keyword = input("Enter a title or author to search: ").strip().lower()
        found_books = []

        for book in library_books:
            # Case-insensitive search in title or author fields
            if keyword in book['title'].lower() or keyword in book['author'].lower():
                found_books.append(book)

        if found_books:
            print(f"\nFound {len(found_books)} result(s):")
            for book in found_books:
                print_book(book)
        else:
            print("No matching books found.")  # Feedback if nothing matches
    except Exception as e:
        print(f"Unexpected error: {e}")  # Catch unexpected issues during search

# Function to display a single book record nicely
def print_book(book):
    status = "Available" if book['available'] else "Checked Out"
    print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {status}")

# Function to list all books in the library
def display_books():
    print("\n--- Library Book List ---")
    if not library_books:
        print("No books in the library.")  # Message for empty list
        return
    try:
        for book in library_books:
            print_book(book)
    except Exception as e:
        print(f"Error displaying books: {e}")  # Catch display errors (if any)

# Function to check out (borrow) a book
def check_out_book():
    print("\n--- Check Out a Book ---")
    try:
        book_id = input("Enter Book ID to check out: ").strip()
        for book in library_books:
            if book['id'] == book_id:
                if book['available']:
                    book['available'] = False  # Mark book as checked out
                    print(f"Book '{book['title']}' checked out successfully.")
                    return
                else:
                    print("This book is already checked out.")  # Prevent double checkout
                    return
        print("Book ID not found.")  # No match found in library
    except Exception as e:
        print(f"Error during check out: {e}")  # Catch all runtime issues

# Function to check in (return) a book
def check_in_book():
    print("\n--- Check In a Book ---")
    try:
        book_id = input("Enter Book ID to return: ").strip()
        for book in library_books:
            if book['id'] == book_id:
                if not book['available']:
                    book['available'] = True  # Mark book as returned
                    print(f"Book '{book['title']}' returned successfully.")
                    return
                else:
                    print("This book is already in the library.")  # Prevent checking in a book already returned
                    return
        print("Book ID not found.")  # Invalid ID
    except Exception as e:
        print(f"Error during check in: {e}")  # Catch-all for unexpected runtime issues

# Main loop that runs the system and handles menu navigation
def run_library_system():
    while True:
        try:
            main_menu()  # Show menu options
            choice = input("Choose an option (1-6): ").strip()

            # Handle menu input and route to correct function
            if choice == '1':
                add_book()
            elif choice == '2':
                search_book()
            elif choice == '3':
                display_books()
            elif choice == '4':
                check_out_book()
            elif choice == '5':
                check_in_book()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.") 
 # Menu #validation
        except Exception as e:
            print(f"An unexpected error occurred: {e}")  # Final fallback for the entire loop




# This ensures the program runs only when executed directly (not when imported as a module).
# I could have simply called the function using run_library_system() and the program would have worked.
# However, using this approach allows the file to be imported (example: import library) without automatically running the system.
# This is considered good practice in Python for better modularity and reusability.

if __name__ == "__main__":
    run_library_system()
