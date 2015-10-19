def main():
	weight_in_pounds = float(input("Enter weight in pounds: "))
	height_in_inches = float(input("Enter height in inches: "))
	weight_in_kg = weight_in_pounds * (0.45359237)
	height_in_meters = height_in_inches * (0.0254)
	bmi = weight_in_kg / (height_in_meters ** 2)
	print ("BMI is %f" % (bmi))

main()