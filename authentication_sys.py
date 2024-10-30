import bcrypt
import secrets
import string
import string
import tkinter as tk
from tkinter import messagebox

# Store user data (use a database or secure file in production)
user_db = {}

def hash_password(password):
    """Generate a bcrypt hash of the password."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def register_user(username, password):
    """Register a new user with a hashed password."""
    if username in user_db:
        print("Username already exists. Please try a different username.")
        return False
    user_db[username] = hash_password(password)
    print(f"User '{username}' registered successfully!")
    return True

def verify_password(stored_password, provided_password):
    """Verify the provided password against the stored hashed password."""
    return bcrypt.checkpw(provided_password.encode(), stored_password)

def login_user(username, password):
    """Login a user by checking if the password matches the stored hash."""
    if username not in user_db:
        print("Username not found.")
        return False
    if verify_password(user_db[username], password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password.")
        return False

def suggest_password(length=12):
    """Generate a strong random password suggestion."""
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

# Setup Tkinter window
root = tk.Tk()
root.title("Authentication System")
root.geometry("400x300")

# Username Label and Entry
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

# Password Label and Entry
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Register Button
register_button = tk.Button(root, text="Register", command=lambda: register_user(username_entry.get(), password_entry.get()))
register_button.pack(pady=10)

# Login Button
login_button = tk.Button(root, text="Login", command=lambda: login_user(username_entry.get(), password_entry.get()))
login_button.pack(pady=10)

#suggest password button
suggest_button = tk.Button(root, text="Suggest Strong Password", command=suggest_password)
suggest_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()