#  File: GuessingGame.py

#  Description: Program to guess a number from 1 to 100

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 11/1/15

#  Date Last Modified: 11/1/15

# Program to do the guessing - based on binary search
def guessing_game(a):
    lo = 0
    hi = len(a)
    turn_number = 1 # to keep track of how many turns it's been
    while (lo <= hi and turn_number < 8):
        mid = (lo + hi) // 2
        # Formatting the statements to print
        print ("Guess %d : The number you thought was %d" % (turn_number, mid))
        verify = int(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
        print ()
        # Series of conditionals to produce the guesses
        if (turn_number == 7 and verify != 0):
            # In case the user messes up or thinks of a number out of range
            print ("Either you guessed a number out of range or you had an incorrect entry.")
            return (-1)
        elif (verify == 1):
            hi = mid - 1
            turn_number += 1
        elif (verify == -1):
            lo = mid + 1
            turn_number += 1
        elif (verify == 0):
            print ("Thank you for playing the Guessing Game.")
            return (mid)

# Define the main function
def main():
    # Series of formatting
    print("Guessing Game")
    print()
    print("Think of a number between 1 and 100 inclusive.")
    print("And I will guess what it is in 7 tries or less.")
    print()
    # Gather the user input
    ready = input("Are you ready? (y/n): ")
    print()
    # Error checking
    while (ready != 'y' and ready != 'n'):
        ready = input("Are you ready? (y/n): ")
    if (ready == 'n'):
        print ("Bye")
        return
    # Encapsulate the rest of the program under this conditional
    elif (ready == 'y'):
        # Create the list to analyze
        a = []
        for i in range(1,101):
            a.append(i)
        # Play the game as defined above
        guessing_game(a)

# Call the main function
main()
