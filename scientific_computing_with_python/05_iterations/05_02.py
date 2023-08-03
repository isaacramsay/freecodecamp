# Exercise 2: Write another program that prompts for a list of numbers as above
# and at the end prints out both the maximum and minimum
# of the numbers instead of the average.

nums = []

while True:
    raw_string = input("Enter a number: ")
    if raw_string == "done":
        break

    try:
        ival = int(raw_string)

    except ValueError:
        print("Please enter a number.")

    else:
        nums.append(ival)

print(f"\nMax number: {max(nums)}\nMin number: {min(nums)}")
