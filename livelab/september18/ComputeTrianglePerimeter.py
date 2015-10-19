def main():
	a,b,c = eval(input("Enter three edges: "))

	if (a + b > c):
		print ("Input is invalid")
	elif (a + c > b):
		print ("Input is invalid")
	elif (b + c > a):
		print ("Input is invalid")

	sum_of_sides = a + b + c
	print ("The perimeter is %.1f" % sum_of_sides)

main()