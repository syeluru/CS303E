def main():

	name = input("Enter employee's name: ")
	hours = float(input("Enter number of hours worked in a week: "))
	pay_rate = float(input("Enter hourly pay rate: "))
	fed_tax_rate = float(input("Enter federal tax withholding rate (as a decimal: "))
	state_tax_rate = float(input("Enter state tax withholding rate (as a decimal: "))

	gross_pay = pay_rate * hours
	fed_tax = (gross_pay) * fed_tax_rate
	state_tax = (gross_pay) * state_tax_rate
	total_deduction = fed_tax + state_tax
	net_pay = gross_pay - total_deduction

	print ("Employee Name: %s" % name)
	print ("Hours Worked: %f" % hours)
	print ("Pay Rate: %f" % pay_rate)
	print ("Gross Pay: %f" % gross_pay)
	print ("Deductions:")
	print ("\tFederal Withholding (%f): $%.2f" % (fed_tax_rate, fed_tax))
	print ("\tState Withoolding (%f): $%.2f" % (state_tax_rate, state_tax))
	print ("Net Pay: %.2f" % net_pay)

main()

