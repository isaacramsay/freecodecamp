# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(score):
    if score > 1.0:
        print("Invalid Score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        print("F")


try:
    score = float(input("Enter score between 0.0 and 1.0: "))

except ValueError:
    print("Please enter a score between 0.0 and 1.0.")

else:
    computegrade(score=score)
