def main():
	sum = 0
	num = 1
	den = 3
	while (num <= 97):
		frac = num/den
		sum += frac
		num += 2
		den += 2
	print (sum)
	return sum

main()