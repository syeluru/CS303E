def main():
	message = ''
	d = 0
	n = 100
	while (n <= 200):
		if (n % 5 == 0 and n % 6 != 0):
			message += "%d " % n
			d += 1
		elif (n % 6 == 0 and n % 5 != 0):
			message += "%d " % n
			d += 1
		if (d == 10):
			message += "\n"
			d = 0
		n += 1
	print (message)
main()