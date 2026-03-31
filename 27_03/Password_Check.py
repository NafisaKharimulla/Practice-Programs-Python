import re

def check_password(password):
    if len(password) < 8:
        return "Weak - Minimum 8 characters required"

    if not re.search("[A-Z]", password):
        return "Weak - Must contain at least one uppercase letter"

    if not re.search("[a-z]", password):
        return "Weak - Must contain at least one lowercase letter"

    if not re.search("[0-9]", password):
        return "Weak - Must contain at least one digit"

    if not re.search("[@#$%^&*]", password):
        return "Weak - Must contain at least one special character"

    return "Strong Password"

password = input("Enter password: ")
print(check_password(password))