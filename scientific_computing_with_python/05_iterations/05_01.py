# Exercise 1: Write a program which repeatedly
# reads numbers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake using
# try and except and print an error message and skip to the next number.

total = 0
count = 0
average = 0

while True:
    raw_string = input("Enter a number: ")
    if raw_string == "done":
        break

    try:
        ival = int(raw_string)

    except ValueError:
        print("Please enter a number.")
        continue

    else:
        total += ival
        count += 1
        average = total/count

print(total, count, average)
