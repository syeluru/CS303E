def main():
	int_to_reverse = (input("Enter an integer: "))
	length = len(int_to_reverse)
	reversed_integer = []
	for i in range(0, length):
		reversed_integer.append(int_to_reverse[i])
	reversed_integer.reverse()
	for i in reversed_integer:
		print (i)
main()