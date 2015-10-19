def determine_day_of_week(day):
	if (day % 7 == 0):
		return "Sunday"
	elif (day % 7 == 1):
		return "Monday"
	elif (day % 7 == 2):
		return "Tuesday"
	elif (day % 7 == 3):
		return "Wednesday"
	elif (day % 7 == 4):
		return "Thursday"
	elif (day % 7 == 5):
		return "Friday"
	elif (day % 7 == 6):
		return "Saturday"

def main():
	today_day = int(input("Enter today's day: "))
	days_from_today = int(input("Enter the number of days elapsed since today: "))

	day_of_week_today = determine_day_of_week(today_day)
	final_day = today_day + days_from_today
	day_of_week_in_future = determine_day_of_week(final_day)

	print (day_of_week_today, day_of_week_in_future) 

main()
							