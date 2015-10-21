#  File: ISBN.py

#  Description: File to verify the validity of a list of ISBN numbers

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 10/19/15

#  Date Last Modified: 10/20/15

# Method for primary error checking
def is_valid_candidate(a):
    if len(a) != 10:
        return False
    elif not a[0:9].isdigit():
        return False
    elif a[0:9].count('x') > 0 or a[0:9].count('X') > 0:
        return False
    else:
        return True
# Method to convert an ISBN string into a list of numbers
def convert_to_list(a):
    # Empty array to start
    b = []
    # Need to append each digit to the array
    for i in range(len(a)):
        # Because we start with a string, need to convert to int
        if a[i].isdigit():
            b.append(int(a[i]))
        # Because we can have an x at the end too, need to add a 10 instead
        elif a[i] == 'x' or a[i] == 'X':
            b.append(10)
    # Need to make it a value-returning function
    return b

# Function to create a list of partial sums from a list of numbers
def partial_sum(a):
    sum = 0
    c = []
    for i in range(len(a)):
        sum += a[i]
        c.append(sum)
    return c

# Function to check if a particular s2 is valid or not
def is_valid_ISBN(s2):
    if s2[9] % 11 == 0:
        return "valid"
    else:
        return "invalid"

def main():
    # Open the file to read
    in_file = open("./isbn.txt", 'r')
    # Open the file to write
    out_file = open("./isbnOut.txt", 'w')
    for line in in_file:
        # Make sure we have just the string without spaces
        # Gets rid of the \n character and any other spaces
        line_to_analyze = line.strip('\n')
        line_to_analyze = line_to_analyze.strip()
        # To get rid of hyphens
        line_to_check = line_to_analyze.replace ("-", "")
        if is_valid_candidate(line_to_check):
            b = convert_to_list(line_to_check)
            # The algorithm
            s1 = partial_sum(b)
            s2 = partial_sum(s1)
            # Each line is in this format:
            line_to_output = "%s  %s \n" % (line_to_analyze, is_valid_ISBN(s2))
            # Write each line out in the new out_file
            out_file.write ("%s" % (line_to_output))
        else:
            out_file.write( "%s invalid \n" % (line_to_analyze))
    # Close both files
    in_file.close()
    out_file.close()

# Call the main function
main()
