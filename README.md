# Python Authentication System

## Overview

This is a simple Python authentication system that allows users to register, log in, and check password strength. It uses the `bcrypt` library for password hashing to ensure that user passwords are stored securely. The application features a graphical user interface (GUI) built with `Tkinter`, providing an interactive experience for users.

## Features

- **User Registration**: Users can create an account by providing a username and password.
- **User Login**: Registered users can log in with their credentials.
- **Password Strength Checker**: Users receive real-time feedback on the strength of their passwords.
- **Password Suggestion**: Users can generate a strong random password suggestion.
- **Secure Password Storage**: Passwords are securely hashed using bcrypt.

## Requirements

To run this project, you need to have Python installed along with the following libraries:

- `bcrypt`
- `tkinter` (usually included with Python)
- `secrets`
- `string`

You can install the required library using pip:

```bash
pip install bcrypt

Usage
Clone the repository to your local machine:
git clone https://github.com/your_username/python-authentication-system.git

Navigate to the project directory:
cd python-authentication-system

Run the application:
python authentication_sys.py

The GUI will open, allowing you to register, log in, and check password strength.

Code Structure
authentication_sys.py: The main application file containing the authentication logic and GUI.

Password Strength Criteria
Weak: Less than 6 characters or lacks complexity (only letters or only numbers).
Medium: At least 6 characters, includes letters and numbers.
Strong: At least 8 characters, includes letters, numbers, and special characters.
Contributing
If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions or suggestions are welcome!

License
This project is open-source and available under the MIT License.

Acknowledgments
Special thanks to the creators of the libraries used in this project.
Inspiration drawn from various resources on password security and GUI development.
