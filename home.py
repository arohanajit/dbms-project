import mysql.connector
import getpass
import sys

def connect_to_database():
    """Establish a connection to the zybooks database."""
    try:
        connection = mysql.connector.connect(
        host='sql5.freemysqlhosting.net',
        port=3306,
        user='sql5740507',     # Replace with your MySQL username
        password='AB4DeU48AR'  # Replace with your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        sys.exit(1)

def display_menu():
    """Display the main menu."""
    print("\nHome")
    print("Display the menu:")
    print("1. Admin Login")
    print("2. Faculty Login")
    print("3. TA Login")
    print("4. Student Login")
    print("5. Exit")

def get_user_choice():
    """Prompt the user to enter a choice between 1 and 5."""
    while True:
        choice = input("\nEnter Choice (1-5): ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        else:
            print("Invalid input. Please enter a numeric value between 1 and 5.")

def validate_user_id(user_id):
    """Validate the user ID format."""
    if not user_id:
        print("User ID cannot be empty.")
        return False
    if len(user_id) > 8:
        print("User ID cannot exceed 8 characters.")
        return False
    return True

def validate_password(password):
    """Validate the password."""
    if not password:
        print("Password cannot be empty.")
        return False
    # You can add more password validation rules here
    return True

def login_user(expected_role):
    """Handle the login process for a user."""
    connection = connect_to_database()
    cursor = connection.cursor()
    cursor.execute("USE sql5740507;")

    while True:
        user_id = input("Enter User ID: ").strip()
        if not validate_user_id(user_id):
            continue

        password = getpass.getpass("Enter Password: ").strip()
        if not validate_password(password):
            continue

        try:
            query = """
            SELECT Role FROM User
            WHERE ID = %s AND Password = %s;
            """
            cursor.execute(query, (user_id, password))
            result = cursor.fetchone()

            if result:
                actual_role = result[0]
                if actual_role.lower() == expected_role.lower():
                    print(f"\nLogin successful. Welcome, {actual_role}!")
                    # Proceed to the appropriate page or function
                    go_to_role_page(actual_role, user_id)
                    break
                else:
                    print(f"\nAccess denied. You are not authorized as a {expected_role}.")
                    # Optionally, you can decide whether to break or allow re-login attempts
                    break
            else:
                print("\nInvalid credentials. Please try again.")
        except mysql.connector.Error as err:
            print(f"Database query error: {err}")
            break
        finally:
            cursor.close()
            connection.close()

def go_to_role_page(role, user_id):
    """Redirect the user to the appropriate page based on their role."""
    pass

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            print("\n--- Admin Login ---")
            login_user('Admin')
        elif choice == 2:
            print("\n--- Faculty Login ---")
            login_user('Faculty')
        elif choice == 3:
            print("\n--- TA Login ---")
            login_user('TA')
        elif choice == 4:
            print("\n--- Student Login ---")
            login_user('Student')
        elif choice == 5:
            print("\nExiting the program. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
