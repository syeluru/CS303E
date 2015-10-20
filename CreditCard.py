#  File: CreditCard.py

#  Description: File to determine validity and idenity of a Credit Card number

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 10/20/15

#  Date Last Modified: 10/20/15

def is_valid(cc_num):
    # Initialize an empty list for splitting up credit card number
    a = []
    b = str(cc_num)

    for i in range(len(b)):
        a.append(b[len(b)-i-1])
    # Initialize an empty list for each digit sum
    for j in range(1,len(a),2):
        # Initialize a variable to keep track of digits' sum
        odd_digits_sum = 0
        a[j] = int(a[j]) * 2
        # add the sum digits of each a[i] to odd_digits_sum
        temp = str(a[j])
        # Sum_digits using a string conversion
        for k in range(len(temp)):
            digit = int(temp[k])
            odd_digits_sum += digit
            a[j] = odd_digits_sum
    # Initialize a total sum variable
    total_sum = 0
    for l in range(len(a)):
        total_sum += int(a[l])
    # Check whether valid or not
    if total_sum % 10 == 0:
        return ("Valid")
    else:
        return ("Invalid")
# Program to determine which type of credit card if valid
def cc_type (cc_num):
    cc_num = str(cc_num)
    # I use string slicing as the easiest way
    if cc_num[:2] == "34" or cc_num[:2] == '37':
        return "American Express"
    elif cc_num[:4] == "6011" or cc_num[:3] == "644" or cc_num[:2] == "65":
        return "Discover"
    elif int(cc_num[:2]) >= 50 and int(cc_num[:2]) <= 55:
        return "MasterCard"
    elif cc_num[0] == '4':
        return "Visa"
    else:
        return ""
# Main function
def main():
    # Prompt user for Credit Card number
    number_to_test = int(eval(input("Enter the credit card number: ")))
    # Check if number is 15 or 16 digits
    if not (len(str(number_to_test)) == 15 or len(str(number_to_test)) == 16):
        print ("Not a 15 or 16-digit number")
        return
    # If invalid credit card:
    elif is_valid(number_to_test) == "Invalid":
        print ("%s credit card number" % is_valid(number_to_test))
    # If valid credit card, then which type
    else:
        print ("%s %s credit card number" % (is_valid(number_to_test), cc_type(number_to_test)))


main()
