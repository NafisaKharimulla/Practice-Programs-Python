s = input("Enter the String: ").lower()
count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
for ch in s:
    if ch in vowels:
        count += 1

print(count)