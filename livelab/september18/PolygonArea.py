import math

def main():
	num_sides = int(input("Enter the number of sides: "))
	side_length = float(input("Enter the side: "))

	area_num = (num_sides * side_length**2)
	area_denom = (4 * math.tan(math.pi/num_sides))
	area = area_num/area_denom

	print("The area of the polgon is %f" % area)

main()