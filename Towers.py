def towers (n, source, spare, dest):
    if n == 1:
        print ("Move disk from", source, "to", dest)
    else:
        # move from source to spare using destination as the spare
        towers (n - 1, source, dest, spare)
        print ("Move disk from", source, "to", dest)
        towers (n - 1, spare, source, dest)
def main():
    towers (3, 'a', 'b', 'c')

main()
'''
A | B
A & B
A - B
A ^ B
'''
