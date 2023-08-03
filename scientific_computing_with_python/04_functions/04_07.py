# Exercise 7: Rewrite the grade program from the
# previous chapter using a function called computegrade
# that takes a score as its parameter and returns
# a grade as a string.

def computegrade(score):
    if score < 0.6:
        return "F"
    elif score < 0.7:
        return "D"
    elif score < 0.8:
        return "C"
    elif score < 0.9:
        return "B"
    elif score <= 1.0:
        return "A"
    else:
        return "Invalid Score."


score = input("Enter score: ")

try:
    score = float(score)

except ValueError:
    print("Please enter a score between 0.0 and 1.0.")

else:
    grade = computegrade(score=score)
    print(grade)
