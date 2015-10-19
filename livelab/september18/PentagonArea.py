import math

def main():
	r = eval(input("Enter the length from center for the pentagon: "))
	
	s = 2 * r * math.sin(math.pi/5)
	area = (5 * s * s / (4 * math.tan(math.pi/5)))
	print ("%.2f" % area)

main()