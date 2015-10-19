def print_palindrome(a):
	#Method that prints the palindrome of a through 1, with a
	#as the starting digit and ending digit
	#Example: print_palindrome(4) should yield 4 3 2 1 2 3 4 
	sequence = ''
	b = a
	while (a > 1):
		sequence += '%d ' % a
		a -= 1
	while (a <= b):
		sequence += '%d ' % a
		a += 1
	return (sequence)

def main():
	num_lines = int(input("Enter the number of lines: "))
	
	for i in range(1,num_lines + 1):
		line = ''
		space_before = "  " * (num_lines - i)
		space_after = space_before
		line += space_before
		line += print_palindrome(i)
		line += space_after
		print (line)

main()