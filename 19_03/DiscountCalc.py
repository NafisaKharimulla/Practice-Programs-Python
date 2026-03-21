amount = float(input())

if amount >= 5000:
    discount = 0.20
elif amount >= 3000:
    discount = 0.10
elif amount >= 1000:
    discount = 0.05
else:
    discount = 0

payable_amount = amount * (1 - discount)

print(int(payable_amount))
