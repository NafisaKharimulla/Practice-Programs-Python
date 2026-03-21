number = input("Enter the number: ")
increasing = True

for i in range(len(number) - 1):
    if int(number[i]) >= int(number[i + 1]):
        increasing = False
        break

if increasing:
    print("Yes")
else:
    print("No")
