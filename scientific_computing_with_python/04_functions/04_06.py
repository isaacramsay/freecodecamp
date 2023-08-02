# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay(hours, rate):
    if hours > 40:
        pay = 40 * rate
        ot_hours = hours - 40
        ot_pay = (rate * 1.5) * ot_hours
        pay = pay + ot_pay
        print("Pay:", pay)
    else:
        print("Pay:", hours * rate)


try:
    hours = int(input("Enter hours: "))
    rate = int(input("Enter pay: "))

except ValueError:
    print("Please enter a number.")

else:
    computepay(hours=hours, rate=rate)
