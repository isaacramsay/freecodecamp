# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

# ! left off here
# TODO OH SHIT THIS IS COOL
# * https://www.freecodecamp.org/learn/scientific-computing-with-python/python-for-everybody/more-conditional-structures

while True:
    try:
        score = float(input("Enter score between 0.0 and 1.0: "))
    except ValueError as e:
        print("Please enter a score between 0.0 and 1.0.")
        continue
    else:
        if score >= 0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >= 0.7:
            print("C")
        elif score >= 0.6:
            print("D")
        else:
            print("F")
