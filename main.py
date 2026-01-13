from management import StudentManagement

def show_menu():
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Students by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("-"*30)

sm = StudentManagement()

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        sm.add_std()
    elif choice == "2":
        sm.view_std()
    elif choice == "3":
        sm.search_std()
    elif choice == "4":
        sm.update_std()
    elif choice == "5":
        sm.delete_std()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")