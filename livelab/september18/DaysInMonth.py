def determine(mon, year):
	is_leap = ((year % 100 != 0 and year % 4 == 0) or (year % 400 == 0))

	if mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
		return ("31 days")
	elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
		return ('30 days')
	elif mon == 2 and is_leap:
		return ('29 days')
	elif mon == 2 and not is_leap:
		return ('28 days')

def main():
	mon = int(input("Enter the month: "))
	year = int(input("Enter the year: "))

	num_days = determine(mon, year)
	if mon == 1:
		month = "January"
	if mon == 2:
		month = "February"
	if mon == 3:
		month = "March"
	if mon == 4:
		month = "April"
	if mon == 5:
		month = "May"
	if mon == 6:
		month = "June"
	if mon == 7:
		month = "July"
	if mon == 8:
		month = "August"
	if mon == 9:
		month = "September"
	if mon == 10:
		month = "October"
	if mon == 11:
		month = "November"
	if mon == 12:
		month = "December"
	
	print ("%s %d has %s" % (month, year, num_days))

main()