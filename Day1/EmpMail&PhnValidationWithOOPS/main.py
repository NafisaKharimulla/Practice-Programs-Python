from employee import Employee


def main():
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        email = input("Enter Employee Email: ")
        phone = input("Enter Employee Phone Number: ")

        emp = Employee(emp_id, name, email, phone)
        emp.display()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
