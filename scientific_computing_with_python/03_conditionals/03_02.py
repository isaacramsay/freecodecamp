# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hours = input("Enter hours: ")
rate = input("Enter pay: ")

try:
    hours = float(hours)
    rate = float(rate)

except ValueError:
    print("Error, please enter numberic input.")

else:
    if hours > 40:
        ot_hours = hours - 40
        ot_pay = (rate * 1.5) * ot_hours
        pay = (rate * 40) + ot_pay

    else:
        pay = hours * rate

    print("Pay:", pay)
