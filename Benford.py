#  File: Benford.py

#  Description: Verifies Benford's Law with Census 2009 data

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 11/23/15

#  Date Last Modified: 11/25/15

def main():
    # Create an empty dictionary
    pop_freq = {}

    # Initialize the dictionary
    pop_freq['1'] = 0
    pop_freq['2'] = 0
    pop_freq['3'] = 0
    pop_freq['4'] = 0
    pop_freq['5'] = 0
    pop_freq['6'] = 0
    pop_freq['7'] = 0
    pop_freq['8'] = 0
    pop_freq['9'] = 0

    # Open file for reading
    infile = open("./census_2009.txt", 'r')

    # Read header
    header = infile.readline()

    # Start counter to decide how many there are total
    counter = 0

    # Read subsequent lines
    for line in infile:
        # Increment counter
        counter += 1
        line = line.strip()
        pop_data = line.split()
        pop_num = pop_data[-1]
        # Add to each respective number's frequency
        if pop_num[0] == '1':
            pop_freq['1'] += 1
        elif pop_num[0] == '2':
            pop_freq['2'] += 1
        elif pop_num[0] == '3':
            pop_freq['3'] += 1
        elif pop_num[0] == '4':
            pop_freq['4'] += 1
        elif pop_num[0] == '5':
            pop_freq['5'] += 1
        elif pop_num[0] == '6':
            pop_freq['6'] += 1
        elif pop_num[0] == '7':
            pop_freq['7'] += 1
        elif pop_num[0] == '8':
            pop_freq['8'] += 1
        elif pop_num[0] == '9':
            pop_freq['9'] += 1

    # Print header
    print ("Digit\tCount\t%")
    for i in range(1,10):
        print ("%d\t%d\t%.1f" % (i, pop_freq[str(i)], 100*(pop_freq[str(i)])/counter))

    infile.close()

main()
