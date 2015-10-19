#  File: DNA.py

#  Description: Program that will read a file with pairs of DNA strands and list the largest common string

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 10/12/15

#  Date Last Modified: 10/14/15

def main():
    # Open file for reading
    in_file = open("./dna.txt", "r")

    # Read number of pairs
    num_pairs = int(in_file.readline().strip())
    print ("Longest Common Sequences\n")
    # Read each pair of DNA strands
    for i in range(num_pairs):
        st1 = in_file.readline()
        st2 = in_file.readline()

        st1 = st1.strip().upper()
        st2 = st2.strip().upper()

        # Order strands by size
        if (len(st1) > len(st2)):
            dna1 = st1
            dna2 = st2
        else:
            dna1 = st2
            dna2 = st1
        # Idea is create a window and make that window smaller when we comapre the two strings
        wind = len(dna2) # The length of the shorter string
        while (wind > 1):
            start_index = 0
            # Initialize a counter variable to keep track
            counter = 0
            # To account for all the sub_strands of a given window size
            while ((start_index + wind) <= len(dna2)):
                sub_strand = dna2[start_index:start_index + wind]
                second_start_index = 0
                # To account for all the sub strands in the second strand of same window size
                while ((second_start_index + wind) <= len(dna1)):
                    second_sub_strand = dna1[second_start_index:second_start_index + wind]
                    # This is to make sure we find any strands that are equal
                    if (second_sub_strand == sub_strand and counter == 0):
                        # Formatting to print the output we want
                        print ("%4s %d: %s" % ("Pair", i + 1, sub_strand))
                        counter += 1
                    elif (second_sub_strand == sub_strand and counter > 0):
                        # Formatting to make sure we don't keep printing "Pair"
                        print ("%7s %s" % ("       ", sub_strand))
                        counter += 1
                    second_start_index += 1
                start_index += 1
            # We don't want the program to keep searching for smaller sub strands if we already have some
            if counter >= 1:
                # This will make the program move on to the next pair
                break
            wind -= 1
        # This will determine if at the end of each pair, there are no common strands
        if counter == 0:
            print ("Pair %d: No Common Sequence Found" % (i + 1))

main()
