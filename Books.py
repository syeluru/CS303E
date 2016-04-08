#  File: Books.py

#  Description: Program to check vocabulary usage of two famous authors

#  Student Name: Sai Yeluru

#  Student UT EID: say346

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date Created: 11/29/15

#  Date Last Modified: 11/29/15

word_dict = {}
def create_word_dict():
    all_words = open('./words.txt', 'r')
    new_file = open('./newfile.txt', 'w')
    for line in all_words:
        word_dict[line] = 1

def parseString(st):
    s = ''
    # If statement to account for all the rules defined
    for ch in range(len(st)):
        if (ch <= len(st) - 2) and ((st[ch].isalpha() and not st[ch] == 's') or st[ch].isspace() or (st[ch] == "'" and (st[ch+1] != 's' or st[ch+1].isspace()))):
            s += st[ch]
        elif (ch >= 1 and st[ch] == 's' and st[ch - 1] != "'"):
            s += st[ch]
        elif (ch >= 1 and st[ch].isspace() and st[ch - 1] == 's'):
            s += ''
        elif ch == len(st) - 1 and (st[ch].isalpha() or st[ch].isspace()) :
            s += st[ch]
        else:
            s += ' '
    # Easy way to split and reconfigure the string
    s_list = s.split()
    final_s = ''
    for x in s_list:
        # Because some words started with an apostrophe
        if not x[0].isalpha():
            final_s += x[1:] + " "
        else:
            final_s += x + " "
    # gives us the final, parsed string
    return (final_s.rstrip())

def getWordFreq(book):
    # Create an empty set for words
    word_set = set()
    # create a dictionary for word frequencies
    word_dict_book = {}
    # track total number of words
    total_words = 0
    for line in book:
        line = line.strip()
        line = line.rstrip('\n')
        # parses the line and removes all extraneous characters
        line = parseString(line)
        # split now
        word_list = line.split()
        # add words to set and dictionary
        for word in word_list:
            word_set.add(word)
            total_words += 1
            if word in word_dict_book:
                word_dict_book[word] += 1
            else:
                word_dict_book[word] = 1
    # close the file
    book.close()
    # creates the list of capital words
    capital_words = []
    # adds all the capital words to this list
    for key in word_dict_book:
        if key[0].isupper():
            capital_words.append(key)
    # goes through the capital word list and fixes the duplicates
    for i in range(len(capital_words)):
        if capital_words[i].lower() in word_dict_book:
            word_dict_book[capital_words[i].lower()] += 1
        # creates an entry if the upper case word is an actual word
        elif capital_words[i].lower() in word_dict:
            word_dict_book[capital_words[i].lower()] = 1
        word_dict_book.pop(capital_words[i], None)
    '''
    for key in word_dict_book:
        print (key + ': ' + str(word_dict_book[key]))
    '''
    return word_dict_book

def wordComparison(author1, wordFreq1, author2, wordFreq2):
    # the first book
    total_words_1 = 0
    for key in wordFreq1:
        total_words_1 += wordFreq1[key]

    # the second book
    total_words_2 = 0
    for key in wordFreq2:
        total_words_2 += wordFreq2[key]

    # create the sets from the dictionaries
    D = set(wordFreq1.keys())
    H = set(wordFreq2.keys())

    # find D - H
    D_minus_H = D - H
    H_minus_D = H - D

    # Distinct words percentage in book 1
    total_distinct_1 = 0
    for key in wordFreq1:
        if key in D_minus_H:
            total_distinct_1 += wordFreq1[key]
    print (author1)
    print ("Total distinct words = " + str(len(wordFreq1)))
    print ("Total words (including duplicates) = " + str(total_words_1))
    print ("Ratio (%% of total distinct words to total words) = %f" % (len(D_minus_H) / total_words_1))
    print ()
    # Distinct words percentage in book 2
    total_distinct_2 = 0
    for key in wordFreq2:
        if key in H_minus_D:
            total_distinct_2 += wordFreq2[key]
    # Print all the outputs
    print (author2)
    print ("Total distinct words = " + str(len(wordFreq2)))
    print ("Total words (including duplicates) = " + str(total_words_2))
    print ("Ratio (%% of total distinct words to total words) = %f" % (len(H_minus_D) / total_words_2))
    print ()

    print ("%s used %d words that %s did not use." % (author1, len(D_minus_H), author2))
    print ("Relative frequency of words used by %s not in common with %s = %f" % (author1, author2, total_distinct_1/total_words_1))
    print ()

    print ("%s used %d words that %s did not use." % (author2, len(H_minus_D), author1))
    print ("Relative frequency of words used by %s not in common with %s = %f" % (author2, author1, total_distinct_2/total_words_2))

def main():
    # create the total word dictionary to be used later
    create_word_dict()
    # ask for user input for book names
    book1_name = input("Enter name of first book: ")
    book2_name = input("Enter name of second book: ")
    print ()

    # ask for user input for author names
    author1 = input ("Enter last name of first author: ")
    author2 = input ("Enter last name of second author: ")
    print ()

    # open the books
    book1 = open(book1_name, 'r')
    book2 = open(book2_name, 'r')

    # Get the frequency of words used by the two authors
    wordFreq1 = getWordFreq(book1)
    wordFreq2 = getWordFreq(book2)

    wordComparison (author1, wordFreq1, author2, wordFreq2)
# Calls the main method
main()
