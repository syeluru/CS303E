# File: Day.py

# Description: Program to determine the day of the week given a year between 1900 and 2100, month, and day

# Student Name: Sai Yeluru

# Student UT EID: say346

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 09/14/2015

# Date Last Modified: 09/14/2015

def main():
	# Gathers the year
	year = int(input("Enter year: "))
	# Checks whether or not the year is a valid year
	while (year < 1900 or year > 2100):
		print ("Please input a valid year")
		year = int(input("Enter year: "))
	# Checks whether or not the year is a leap year		
	if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
		is_Leap_Year = True
	else:
		is_Leap_Year = False	

	# Code to assign the month
	month = int(input("Enter month: "))
	# Error checking to ensure it's a valid month
	while (month < 1 or month > 12):
		print ("Please input a valid month: 1 - 12")
		month = int(input("Enter month: "))
	# Assigns the correct valuables to a and c given year and month
	if month >= 3:
		a = month - 2
		c = year % 100
		year_was_changed = False
	else:
		a = month + 10
		c = (year - 1) % 100
		year_was_changed = True

	# Gathers input for day and assigns it to variable b
	b = int(input("Enter day: "))
	# Determines whether day is valid or not
	if (month == 1 or month == 3 or month == 5 or month == 7 or 
		month == 8 or month == 10 or month == 12):
		while b < 1 or b > 31:
			print ("Please input a valid day")
			b = int(input("Enter day: "))
	elif month == 4 or month == 6 or month == 9 or month == 11:
		while b < 1 or b > 30:
			print ("Please input a valid day")
			b = int(input("Enter day: "))
	elif month == 2:
		if is_Leap_Year:
			while b < 1 or b > 29:
				print ("Please input a valid day")
				b = int(input("Enter day: "))
		else: 
			while b < 1 or b > 28:
				print ("Please input a valid day")
				b = int(input("Enter day: "))

	# Command to assign the value for d
	if year_was_changed:
		d = (year - 1) // 100
	else: 
		d = year // 100

	# The algorithms to determine the day of the week given a, b, c, and d
	w = (13 * a - 1) // 5
	x = c // 4
	y = d // 4
	z = w + x + y + b + c - 2 * d
	r = z % 7
	r = (r + 7) % 7

	# The code to determine the day of the week based on r
	if r == 0:
		day = "Sunday"
	elif r == 1:
		day = "Monday"
	elif r == 2:
		day = "Tuesday"
	elif r == 3:
		day = "Wednesday"
	elif r == 4:
		day = "Thursday"
	elif r == 5:
		day = "Friday"
	elif r == 6:
		day = "Saturday"

	print ("") #to insert empty line
	# And now the final statement:
	print ("The day is %s" % day)

# Calls the main function to execute the program
main()