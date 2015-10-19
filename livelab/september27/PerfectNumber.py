def main():
	n = 2
	while (n < 10000):
		sum = 0
		for i in range (1, n):
			if (n % i) == 0:
				sum += i
		if sum == n:
			print (n)
		n += 1

main()