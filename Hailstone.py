#  File: Hailstone.py

#  Description: Program to compute the maximum cycle length of a Hailstone sequence given a range of numbers

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 09/18/15

#  Date Last Modified: 09/18/15

def hailstone(num):
	counter = 0
	while (num != 1):
		if (num % 2 == 0):
			num = num // 2
		else: 
			num = (num * 3) + 1
		counter += 1
	return (counter)

def main():
	# Gather user input
	start_num = int(input("Enter starting number of the range: "))
	end_num = int(input("Enter ending number of the range: "))
	max_cycle_length = 0
	while (start_num <= end_num):
		cycle_length = hailstone(start_num)
		if (cycle_length >= max_cycle_length):
			largest_number = start_num
			max_cycle_length = cycle_length		
		start_num += 1

	print ("The number %d has the longest cycle length of %d"\
		% (largest_number, max_cycle_length))

main()