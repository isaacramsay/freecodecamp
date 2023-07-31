# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

while True:
    try:
        hours = int(input("Enter hours: "))
        rate = int(input("Enter pay: "))

    except ValueError as e:
        print("Please enter a number.")
        continue

    else:
        if hours > 40:
            pay = 40 * rate
            ot_hours = hours - 40
            ot_pay = (rate * 1.5) * ot_hours
            pay = pay + ot_pay
            print("Pay:", pay)
        else:
            print("Pay:", hours * rate)
    break