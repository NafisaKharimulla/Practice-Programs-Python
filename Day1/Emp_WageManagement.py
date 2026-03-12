# Employee Wage and Data Management Program

def get_employee_data():
    try:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary_per_hour = float(input("Enter Salary per Hour: "))

        hours = []
        print("Enter working hours for 7 days:")

        for i in range(1, 8):
            h = float(input(f"Day {i} hours: "))
            hours.append(h)

        return emp_id, name, salary_per_hour, hours

    except ValueError:
        print("Invalid input! Please enter numeric values for hours and salary.")
        return None


def calculate_weekly_wage(hours, salary_per_hour):
    total_hours = sum(hours)

    # Bonus condition
    if total_hours > 40:
        bonus = 500
    else:
        bonus = 0

    total_wage = (total_hours * salary_per_hour) + bonus
    return total_hours, total_wage, bonus


def save_to_file(employee_record):
    with open("employee_records.txt", "a") as file:
        file.write(str(employee_record) + "\n")


def main():
    print("=== Employee Wage Management System ===")

    data = get_employee_data()

    if data is None:
        return

    emp_id, name, salary_per_hour, hours = data

    # List comprehension to calculate daily wages
    daily_wages = [h * salary_per_hour for h in hours]

    total_hours, total_wage, bonus = calculate_weekly_wage(hours, salary_per_hour)

    # Storing data in dictionary
    employee = {
        "ID": emp_id,
        "Name": name,
        "Hours": hours,
        "Daily Wages": daily_wages,
        "Total Hours": total_hours,
        "Bonus": bonus,
        "Total Wage": total_wage
    }

    print("\nEmployee Weekly Summary:")
    for key, value in employee.items():
        print(f"{key}: {value}")

    # Save record to file
    save_to_file(employee)

    print("\nRecord saved successfully to employee_records.txt")


if __name__ == "__main__":
    main()
