def convert_to_list(a):
    # Empty array to start
    b = []
    # Need to append each digit to the array
    for i in range(len(a)):
        if a[i].isdigit():
            b.append(int(a[i]))
        elif a[i] == 'x' or a[i] == 'X':
            b.append(10)
def is_valid(b):
    if a[9] % 11 == 0:
        return True
    else:
        return False

def main():
