# File: Goldbach.py

# Description: Program to display the Goldbach effect on any even number in a given range

# Student Name: Sai Yeluru

# Student UT EID: say346

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 09/22/2015

# Date Last Modified: 09/22/2015



# Defines the is_prime function as defined in class

def is_prime (n):
	limit = int (n ** 0.5) + 1
	divisor = 2
	while (divisor < limit):
		if (n % divisor == 0):
			return False
		divisor = divisor + 1
	return True

def main():
	# Get the user input
	lower_limit = int(input("Enter the lower limit: "))
	while (lower_limit % 2 != 0 or lower_limit < 4): 
		print ("Please enter an even number greater than 4.")
		lower_limit = int(input("Enter the lower limit: "))
	upper_limit = int(input("Enter the upper limit: "))
	while (upper_limit % 2 != 0 or lower_limit >= upper_limit):
		print ("Please enter an even number greater than the lower limit.")
		upper_limit = int(input("Enter the upper limit: "))
	# Error checking above

	# While loop to run from lower_limit to upper_limit
	while (lower_limit <= upper_limit):
		# Initialize dummy terms to add for each even number
		# Start at 2 because 2 is first prime number
		a = 2
		b = lower_limit - a
		message = ''
		# Inner loop to compute the actual values of a and b 
		while (a <= b):
			if (is_prime(a) and is_prime(b) and lower_limit == a + b):
				message += ("= %d + %d " % (a, b))
			a += 1
			b = lower_limit - a
		# Outside the inner loop so as to only print the message we want
		print ("%d %s" % (lower_limit, message))
		lower_limit += 2
		
main()