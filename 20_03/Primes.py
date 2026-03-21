import math

A = int(input()) #Starting Range
B = int(input()) #Ending Range

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

count = 0
for num in range(A, B + 1):
    if is_prime(num):
        count += 1

print(count)
