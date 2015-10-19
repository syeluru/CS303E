def main():
	monthly_contribution = float(input("Enter the monthly saving amount: "))
	annual_interest_rate = 0.05
	monthly_interest_rate = annual_interest_rate/12
	savings = 0
	for i in range(0,6):
		savings = (monthly_contribution + savings) * (1 + monthly_interest_rate)

	print ("After the sixth month, the account value is %f" % savings)

main()