marks = list(map(int, input().split()))

if any(mark < 35 for mark in marks):
    print("FAIL")
else:
    average = sum(marks) / len(marks)
    if average >= 75:
        print("DISTINCTION")
    else:
        print("PASS")
