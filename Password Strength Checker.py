import re

password = input("Enter a password: ")

errors = []

if len(password) < 8:
    errors.append("Password must be at least 8 characters long.")

if not re.search(r"[A-Z]", password):
    errors.append("Password must contain at least one uppercase letter.")

if not re.search(r"[0-9]", password):
    errors.append("Password must contain at least one number.")

if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    errors.append("Password must contain at least one special character.")

if not errors:
    print("Strong Password ")
else:
    print("Weak Password ")
    for error in errors:
        print("-", error)