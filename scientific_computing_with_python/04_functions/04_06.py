# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate
        ot_hours = hours - 40
        ot_pay = (rate * 1.5) * ot_hours
        pay = pay + ot_pay

    else:
        pay = hours * rate

    return pay


hours = input("Enter hours: ")
rate = input("Enter pay: ")

try:
    hours = float(hours)
    rate = float(rate)

except ValueError:
    print("Please enter a number.")

else:
    pay = computepay(hours=hours, rate=rate)
    print("Pay:", pay)
