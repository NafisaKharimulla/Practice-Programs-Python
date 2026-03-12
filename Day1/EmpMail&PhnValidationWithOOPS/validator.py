import re

# Custom Exceptions
class InvalidEmailException(Exception):
    pass

class InvalidPhoneException(Exception):
    pass


# Function to validate email using regex
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not re.match(pattern, email):
        raise InvalidEmailException("Invalid Email Format")

    return True


# Function to validate phone using regex
def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'   # 10 digit Indian phone number

    if not re.match(pattern, phone):
        raise InvalidPhoneException("Invalid Phone Number")

    return True
