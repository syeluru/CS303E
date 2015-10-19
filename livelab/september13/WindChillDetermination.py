def main():
  	temp_outside = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
  	while (temp_outside <= -58 or temp_outside >= 41):
  		print("Please input a temperature between -58 and 41 degrees Fahrenheit")
  		temp_outside = float(input("Enter the temperature in Fahrenheit between -58 and 41: "))
  	wind_speed = float(input("Enter the wind speed in miles per hour: "))
  	windchill_temp = (35.74 + 0.6215*temp_outside - 35.75*(wind_speed**0.16) + .4275*temp_outside*(wind_speed**0.16))

  	print("The wind chill index is %.5f" % windchill_temp)

main()