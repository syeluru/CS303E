def squares_palindrome(a):
	#Method that prints the palindrome of 1 through 2 ** (a - 1), with a
	#as the starting digit and ending digit
	#Example: squares_palindrome(4) should yield 1 2 4 8 4 2 1  
	sequence = ''
	
	counter = a
	while (a > 1):
		b = 2 ** (counter - a)
		sequence += '%d ' % b
		a -= 1
	while (a <= counter):
		b = 2 ** (counter - a)
		sequence += '%d ' % b
		a += 1
	return (sequence)

def main():
	#num_lines = int(input("Enter the number of lines: "))
	num_lines = 8
	for i in range(1,num_lines + 1):
		line = ''
		space_before = "  " * (num_lines - i)
		space_after = space_before
		line += space_before
		line += squares_palindrome(i)
		line += space_after
		print (line)

main()
