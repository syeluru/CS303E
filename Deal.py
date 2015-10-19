# File: Deal.py

# Description: Simulation of "Let's make a deal" to prove that switching is alwasy the better option

# Student Name: Sai Yeluru

# Student UT EID: say346

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 09/30/15

# Date Last Modified: 09/30/15

# Imports the required module
import random
# Defines a function to make printing each line easier
def printLine(prize, guess, view, new_guess):
    line_to_print = "%5d%11d%11d%11d" % (prize, guess, view, new_guess)
    print (line_to_print)
# Defines the main function
def main():
    num_plays = int(input("How many times would you like to play: "))
    # Print the header line
    header_line = "%7s%11s%11s%13s" % ("Prize", "Guess", "View", "New Guess")
    print (header_line)
    # Counter variable
    wins_by_switching = 0
    # For loop to determine success or failure
    for i in range(num_plays):
        prize = random.randint(1,3)
        guess = random.randint(1,3)
        false_door = random.randint(1,3)
        # While loop to check that the false_door is indeed false
        while (false_door == prize or false_door == guess):
            false_door = random.randint(1,3)
        new_guess = random.randint(1,3)
        # While loop to check that the new guess is not one
        # that was false or previously picked
        while (new_guess == false_door or new_guess == guess):
            new_guess = random.randint(1,3)
        if (new_guess == prize):
            wins_by_switching += 1
        printLine(prize,guess,false_door,new_guess)

    # Variable to determine probability of winning by switching
    prob_win_by_switch = wins_by_switching/num_plays
    # Variable to determine probability of winning by not switching
    prob_win_not_switch = 1 - prob_win_by_switch
    print () # to print an empty line
    print ("Probability of winning if you switch = %.2f" % prob_win_by_switch)
    print ("Probability of winning if you do not switch = %.2f" % prob_win_not_switch)

main()
