from validator import validate_email, validate_phone


class Employee:

    def __init__(self, emp_id, name, email, phone):

        self.emp_id = emp_id
        self.name = name

        # Validate email and phone before assigning
        validate_email(email)
        validate_phone(phone)

        self.email = email
        self.phone = phone


    def display(self):
        print("\nEmployee Details:")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Phone:", self.phone)
