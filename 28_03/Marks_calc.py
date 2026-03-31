students = {}

def add_student(name, marks):
    students[name] = marks

def display_students():
    for name, marks in students.items():
        print(name, ":", marks)

def find_topper():
    topper = max(students, key=students.get)
    print("Topper:", topper, "with", students[topper])

add_student("Rahul", 85)
add_student("Anita", 92)
add_student("Kiran", 78)

display_students()
find_topper()