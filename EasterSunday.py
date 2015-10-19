# File: EasterSunday.py

# Description: This program computes the date that Easter Sunday falls on for any year. 

# Student Name: Sai Yeluru

# Student UT EID: say346

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 06 September 2015

# Date Last Modified: 06 September 2015

def main():
  # Prompts the user to input the year to test
  y = int(input("Enter year: "))
  
  # The calculations necessary to determine the month and date 
  a = y % 19
  b = y // 100
  c = y % 100
  d = b // 4
  e = b % 4
  g = ((8 * b) + 13) // 25
  h = ((19 * a) + b - d - g + 15) % 30
  j = c // 4
  k = c % 4
  m = (a + (11 * h)) // 319
  r = ((2 * e) + (2 * j) - k - h + m + 32) % 7
  
  # n and p represent the month and date (respectively)
  n = (h - m + r + 90) // 25
  p = (h - m + r + n + 19) % 32
  
  # If statement to insert March or April into the final statement.
  # An elif and else were added to account for all possibilities.
  if (n == 3):
    month = "March"
  elif (n == 4):
    month = "April"
  else: 
    month = ""
  
  # Prints the final statement
  print ("In %d Easter Sunday is on %d %s." % (y, p, month))

# Calls the main function to execute the program.
main()