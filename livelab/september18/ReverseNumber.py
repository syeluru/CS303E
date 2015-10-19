def rev_num (n):
  rev_n = 0
  while (n > 0):
    rev_n = rev_n * 10 + n % 10
    n = n // 10
  return rev_n

def main():
	num = int(input("Enter a number to reverse: "))
	print (rev_num (num))

main()