def sum_divisors (n):
  if (n == 1):
    return 0
  sum_d = 0
  limit = n // 2 + 1
  for div in range (1, limit):
    if (n % div == 0):
      sum_d += div
  return sum_d


def main():
    d = 0
    for i in range(1,10001):
        m = sum_divisors(i)
        if m != i:
            if sum_divisors(m) == i and sum_divisors(m) != d:
                print (i,m)
                d = m
                # b = a

main()
