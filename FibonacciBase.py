#  File: FibonacciBase.py

#  Description: Program to represent a base 10 number in a fibonacci base

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 11/8/15

#  Date Last Modified: 11/8/15

# Method to identify the nth fibonacci number
def identify_nth_fib(n):
    if n < 2:
        return n
    prev = 1
    current = 1
    for i in range (2, n):
        prev, current = current, current + prev
    return current

# Method to create a fibonacci sequence based on the nth fibonacci number
def create_fib_seq(n):
    i = 2
    seq = []
    fib = 0
    while fib < n:
        fib = identify_nth_fib(i)
        seq.append(fib)
        i += 1
    # Removes the last number because it's greater than our number to convert
    seq.pop(-1)
    # Reverses the sequence to go in descending order
    seq.reverse()
    return seq

# Method to convert the number of interest to a number in base fibonacci
def convert_fib_base(num):
    fib_seq = create_fib_seq(num)
    fib_str = ""
    for i in range(len(fib_seq)):
        if num >= fib_seq[i]:
            num = num - fib_seq[i]
            fib_str += "1"
        else:
            fib_str += "0"
    return fib_str

# The main method to actually print the sequence
def main():
    num = int(input("Enter a number: "))
    fib_repr = (convert_fib_base(num))
    print ("%i = %s (fib)" % (num, fib_repr))
# Calls the main method
main()
