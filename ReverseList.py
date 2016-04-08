def reverse_list(some_list):
    for i in range(len(some_list)):
        for j in range(len(some_list[i])//2):
            some_list[i][j],some_list[i][len(some_list[i])-j-1] = some_list[i][len(some_list[i])-j-1], some_list[i][j]
        #some_list[i] = some_list[i].reverse()
    return some_list

def main():
    print (reverse_list([[1,2,3,4],[2,3,4,1]]))

main()
