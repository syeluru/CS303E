# File: Grid.py

# Description: Program to compute the largest product whether in a row, column, or diagonal going from left to right of four numbers consecutively

# Student Name: Sai Yeluru

# Student UT EID: say346

# Course Name: CS 303E

# Unique Number: 50475

# Date Created: 10/26/15

# Date Last Modified: 10/26/15

# Product of 4 consecutive numbers in a row
def prod_4_in_rows(b):
    max_prod = 1
    window = 4
    for i in range(len(b)):
        go_until = len(b[i]) - window
        for j in range(go_until+1):
            prod = 1
            for k in range(window):
                prod = prod * b[i][j+k]
            if prod >= max_prod:
                max_prod = prod
    return max_prod

# Product of 4 consecutive numbers in a column
def prod_4_in_cols(b):
    max_prod = 1
    window = 4
    for j in range(len(b[0])):
        go_until = len(b[0]) - window
        for i in range(go_until+1):
            prod = 1
            for k in range(window):
                prod = prod * b[i + k][j]
            if prod >= max_prod:
                max_prod = prod
    return max_prod

# Define a method to calculate the product from left to right
# of 4 in a diagonal given starting row and column index
def diag_product_left_to_right(start_row, start_col, b):
    product = 1
    for i in range(4):
        product = product * b[start_row+i][start_col+i]
    return product

# Using the above method, find the maximum diagonal product
# going from left to right
def prod_4_in_diag_left_to_right(b):
    window = 4
    max_prod = 1
    for i in range(len(b)-window+1):
        for j in range(len(b[i])-window+1):
            # Compute diagonal product starting at this location
            prod = diag_product_left_to_right(i,j,b)
            if prod >= max_prod:
                max_prod = prod
    return max_prod

# Define a method to calculate the product from right to left
# of 4 in a diagonal given starting row and column index
def diag_product_right_to_left(start_row, start_col, b):
    product = 1
    for i in range(4):
        product = product * b[start_row+i][start_col-i]
    return product

# Using the above method, find the maximum diagonal product
# going from right to left
def prod_4_in_diag_right_to_left(b):
    window = 4
    max_prod = 1
    for i in range(len(b)-window+1):
        for j in range(len(b)-1, window-2,-1):
            prod = diag_product_right_to_left(i,j,b)
            if prod >= max_prod:
                max_prod = prod
    return max_prod

# Function to return the maximum of the four possible max products
def maximize(a,b,c,d):
    max = a
    if b >= max:
        max = b
    if c >= max:
        max = c
    if d >= max:
        max = d
    return max


def main():
    #gridfile = open("./grid.txt", 'r')
    gridfile = open("./grid.txt", 'r')
    dim = gridfile.readline()
    dim = int(dim)
    grid = []
    # Read data line by line
    for i in range(dim):
        line = gridfile.readline()
        line = line.strip()
        nums = line.split()
        # Convert into integers
        for j in range(dim):
            nums[j] = int(nums[j])
        grid.append(nums)
    # Now we have our 2D grid of numbers

    a = (prod_4_in_rows(grid))
    b = (prod_4_in_cols(grid))
    c = (prod_4_in_diag_left_to_right(grid))
    d = (prod_4_in_diag_right_to_left(grid))
    max_product_overall = maximize(a,b,c,d)
    print ("The greatest product is %d." % max_product_overall)


    # Closes the file.
    gridfile.close()

main()
