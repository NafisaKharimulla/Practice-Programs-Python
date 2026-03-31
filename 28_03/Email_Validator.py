import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")

email = input("Enter email: ")
validate_email(email)