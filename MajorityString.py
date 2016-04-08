def majority(string):
    b = []
    for i in range(len(string)):
        b.append(string[i])
    b.sort()
    count = 0
    for i in range(len(b)):
        count = b.count(b[i])
        if count > (len(b) // 2):
            return True
    return False

def main():
    print (majority("affffbbbbbbbbaa"))

main()
