marks = list(map(int, input("Enter 5 subject marks: ").split()))
avg = sum(marks) / len(marks)

if avg >= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")