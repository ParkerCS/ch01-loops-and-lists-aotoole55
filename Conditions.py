# nice solutions

#CONDITIONS (15PTS TOTAL)

# PROBLEM 1 (GPA - 4pts)
# Grades are values between 0 and 100
# We will translate grades to letters using:
# http://www.collegeboard.com/html/academicTracker-howtoconvert.html
# Make a variable for your percentage grade.
# Make a series of if/elif/else statements to print the letter grade.
# If the user enters a grade lower than zero or higher than 100, just give an error message.
# Don't worry about making an exception for these right now.

def grade():
    grade = int(input("Enter your grade between 0 and 100: "))
    if grade >= 97:
        print("You have an A+.")
    elif grade >= 93:
        print("You have an A.")
    elif grade >= 90:
        print("You have an A-.")
    elif grade >= 87:
        print("You have an B+.")
    elif grade >= 83:
        print("You have an B.")
    elif grade >= 80:
        print("You have an B-.")
    elif grade >= 77:
        print("You have an C+.")
    elif grade >= 73:
        print("You have an C.")
    elif grade >= 70:
        print("You have an C-.")
    elif grade >= 67:
        print("You have an D+.")
    elif grade >= 65:
        print("You have an D.")
    elif grade < 65 and grade >= 0:
        print("You have an E/F.")
    else:
        print("Error.")

grade()


# PROBLEM 2 (Vowels - 5pts)
# Ask the user to supply a string.
# Print how many different vowels there are in the string.
# The capital version of a lower case vowel is considered to be the same vowel.
# y is not considered a vowel.
# Try to print proper output (e.g., printing “There are 1 different vowels in the string” is ugly).
# Example: When the user enters the string “It’s Owl Stretching Time,”
# the program should say that there are 3 different vowels in the string.

def counter():
    string = str(input("Enter a string: "))
    string = string.lower()
    number_of_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in range(len(string)):
        if 'a' in vowels and 'a' == str(string[i]): #found if 'a' in vowels online: http://stackoverflow.com/questions/12934190/is-there-a-short-contains-function-for-lists
            number_of_vowels += 1
            vowels.remove('a')
        elif 'e' in vowels and 'e' == str(string[i]):
            number_of_vowels += 1
            vowels.remove(str('e'))
        elif 'i' in vowels and 'i' == str(string[i]):
            number_of_vowels += 1
            vowels.remove('i')
        elif 'o' in vowels and 'o' == str(string[i]):
            number_of_vowels += 1
            vowels.remove('o')
        elif 'u' in vowels and 'u' == str(string[i]):
            number_of_vowels += 1
            vowels.remove('u')

    if number_of_vowels == 1:
        print("There is 1 vowel in your string.")
    elif number_of_vowels != 1:
        print("There are", number_of_vowels, "vowels in your string.")

counter()

# PROBLEM 3 (Quadratic Equation - 6pts)
# You can solve quadratic equations using the quadratic formula.
# Quadratic equations are of the form Ax2 + Bx + C = 0.
# Such equations have zero, one or two solutions.
# The first solution is (−B + sqrt(B^22 − 4AC))/(2A).
# The second solution is (−B − sqrt(B^2 − 4AC))/(2A).
# There are no solutions if the value under the square root is negative.
# There is one solution if the value under the square root is zero.
# Write a program that asks the user for the values of A, B, and C,
# then reports whether there are zero, one, or two solutions,
# then prints those solutions.
# Note: Make sure that you also take into account the case that A is zero,
# and the case that both A and B are zero.
import math

a = int(input("Enter an A value: "))

b = int(input("Enter a B value: "))

c = int(input("Enter a C value: "))

def quad_solver():
    if a == 0 and b != 0:
        print("Linear equation inputted. One solution. Solution lies at x =", -c/b)
    elif a == 0 and b == 0:
        print("Indeterminate.")
    elif (b**2 - 4*a*c) < 0:
        print("No solutions.")
    elif (b**2 - 4*a*c) == 0:
        print("Only solution lies at:", -b / (2*a))
    else:
        print("Two solutions found.")
        print("Solution 1 lies at x =", round((-b + math.sqrt(b**2 - 4*a*c)) / (2*a),2))
        print("Solution 1 lies at x =", round((-b - math.sqrt(b**2 - 4*a*c)) / (2*a),2))

quad_solver()