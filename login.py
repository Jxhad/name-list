import tkinter as tk
import mysql.connector


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("300x150")

        self.login_label = tk.Label(root, text="Login")
        self.login_label.pack()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.signin_button = tk.Button(root, text="Sign In", command=self.signin)
        self.signin_button.pack()

        self.signup_button = tk.Button(
            root, text="Sign Up", command=self.open_registration_window
        )
        self.signup_button.pack()

        # Instance variable to store registration window
        self.registration_window = None

        # Establish a connection to the MySQL database
        self.connection = mysql.connector.connect(
            host="localhost", user="root", password="Jehadqwwq1221", database="account"
        )
        self.cursor = self.connection.cursor()

    def signin(self):
        # Get username and password from entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the database for the entered username and password
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        user_data = (username, password)
        self.cursor.execute(query, user_data)

        # Fetch the result
        result = self.cursor.fetchone()

        # Check if the result is not None, indicating successful login
        if result:
            print("Login successful!")
            # Here you can add logic to open another window or perform other actions after successful login
        else:
            print("Invalid credentials")

    def open_registration_window(self):
        self.registration_window = tk.Toplevel(self.root)
        self.registration_window.title("Registration Window")
        self.registration_window.geometry("300x150")

        registration_label = tk.Label(self.registration_window, text="Registration")
        registration_label.pack()

        username_label = tk.Label(self.registration_window, text="Username:")
        username_label.pack()
        self.reg_username_entry = tk.Entry(self.registration_window)
        self.reg_username_entry.pack()

        password_label = tk.Label(self.registration_window, text="Password:")
        password_label.pack()
        self.reg_password_entry = tk.Entry(self.registration_window, show="*")
        self.reg_password_entry.pack()

        register_button = tk.Button(
            self.registration_window,
            text="Register",
            command=self.register_and_close_registration,
        )
        register_button.pack()

    def register_and_close_registration(self):
        # Get username and password from entry fields
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()

        # Insert user data into the 'users' table
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        user_data = (username, password)
        self.cursor.execute(insert_query, user_data)
        self.connection.commit()

        # Close registration window and open login window
        self.root.deiconify()  # Show login window
        self.registration_window.destroy()  # Close registration window

    def __del__(self):
        self.cursor.close()
        self.connection.close()


# Create the main application window (login window)
root = tk.Tk()
login_window = LoginWindow(root)

# Run the main loop
root.mainloop()
