salary = float(input())
late_days = int(input())
absent_days = int(input())

deduction_rate = 0

if late_days > 5:
    deduction_rate += 0.05
if late_days > 10:
    deduction_rate += 0.10
if absent_days > 2:
    deduction_rate += 0.05

final_salary = salary * (1 - deduction_rate)

print(int(final_salary))
