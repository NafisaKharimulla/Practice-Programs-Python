numbers = list(map(int, input("Enter numbers: ").split()))
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Without duplicates:", unique)