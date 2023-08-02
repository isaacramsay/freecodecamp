# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))
if hours > 40:
    ot_time = hours - 40
    ot_rate = rate * 1.5
    ot_pay = ot_time * ot_rate
    pay = (rate * 40) + ot_pay
else:
    pay = hours * rate

print("Pay:", pay)
