#  File: CalculatePI.py

#  Description: Program to approximate Pi using random numbers

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 09/30/15

#  Date Last Modified: 09/30/15

# Imports the required modules
import math
import random

# Function to compute Pi based on random numbers
def computePI (numThrows):
    count_inside = 0
    total_num_throws = 0
    # For loop to determine whether a random
    # "throw" is inside the circle
    for i in range (1, numThrows + 1):
        radius = 1.0
        xPos = random.uniform(-1.0, 1.0)
        yPos = random.uniform(-1.0, 1.0)
        dist_from_center = math.hypot(xPos, yPos)
        if (dist_from_center < radius):
            count_inside += 1
        total_num_throws += 1
    # Computes our approximate value of pi
    pi_approx = (count_inside/total_num_throws) * 4
    # Returns the pi value for use in main function
    return pi_approx

# Method to make printing of lines easier
def printLine (line_number):
    # Code to determine the number of iterations from the line number
    num = 10 ** (line_number + 1)
    first_part = "num = %d" % (num)
    # The second part of the line: the calculated number
    second_part = "Calculated PI = %.6f" % (computePI(num))
    # Code to print the difference part of each line
    difference = computePI(num) - math.pi
    if (difference > 0):
        last_part = "Difference = +%f" % difference
    else:
        last_part = "Difference = %f" % difference
    # The message we want to print
    message = "%-14s  %27s  %22s" % (first_part,second_part,last_part)
    print (message)

# Call the main function
def main():
    # For loop to print each line
    for i in range (1, 7):
        printLine(i)
    print("Difference = Calculated PI - math.pi")

# Calls the main function
main()
