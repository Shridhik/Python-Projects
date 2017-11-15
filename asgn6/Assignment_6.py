#!/usr/bin/python3
# coding=utf-8
#
# Assignment 6
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu


import os.path                             # will return true if the file exists (found on course web page)
comb_hist_words ={}                        # dictionary for global combined histogram of words
comb_hist_char ={}                         # dictionary for global combined hisotgram of characters
comb_hist_bi ={}
comb_hist_tri ={}
comb_tot_word = 0                           # initialzing the global variables
comb_tot_char = 0
comb_tot_bi   = 0
comb_tot_tri = 0

comb_list_words =[]                         # List for the cumulative list
comb_list_char =[]
comb_list_bi =[]
comb_list_tri =[]

def openfile():                            # function that opens file

    aval = False
    while not aval:
        filename = input("What file do you want to import? ", )         # user input for files being opened, stored into variable
        aval = os.path.isfile(filename)                                 # will make sure the file entered exists
        if aval:                                                        #program that runs if available
            return filename                                             # will return filename if available
        if len(filename)<1:                                             #if the user just enters return the program will run
            break
        elif not aval:                                                  # if the program does not exist, a print statement will indicate so
            print("I don't recognize the file,", filename, "Try Again!!!")

            print("")                                                   # a space just to make the program look neat

    return

def allfile():                                                          # program that runs all files
    i=1                                                                 # i will initialize the number of file counter
    fname1=""                                                           # initializes file name string
    fname2=""
    fname3=""
    fname4=""
    fname5=""
    fname6=""
    fname7=""
    fname8=""
    fname9=""
    fname10=""
    while i <= 10:                                                      # while loop that loops up to ten files
        if i == 1:                                                      # the first file that should run
            fname1 = openfile()                                         # function created earlier that opens file, and stores file in fname1
            print("First file is: ", fname1)                            # prints the file name
            print("PRESS ENTER WHEN DONE ENTERING FILES")               # reminds user to press enter when ready to run program
            print("")

            if not fname1:                                              # if we press enter, the program will break and run
                break
            else:                                                       # else, we will continue adding 1 to i, which will request more files
                i += 1

        elif i == 2:
            fname2 = openfile()
            print("Second file=", fname2)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname2:
                break
            else:
                i += 1

        elif i == 3:
            fname3 = openfile()
            print("Third file=", fname3)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname3:
                break
            else:
                i += 1

        elif i == 4:
            fname4 = openfile()
            print("Fourth file=", fname4)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname4:
                break
            else:
                i += 1

        elif i == 5:
            fname5 = openfile()
            print("Fifth file=", fname5)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname5:
                break
            else:
                i += 1

        elif i == 6:
            fname6 = openfile()
            print("Sixth file=", fname6)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname6:
                break
            else:
                i += 1

        elif i == 7:
            fname7 = openfile()
            print("Seventh file=", fname7)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname7:
                break
            else:
                i += 1

        elif i == 8:
            fname8 = openfile()
            print("Eighth file=", fname8)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname8:
                break
            else:
                i += 1

        elif i == 9:
            fname9 = openfile()
            print("Ninth file=", fname9)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname9:
                break
            else:
                i += 1

        elif i == 10:
            fname10 = openfile()
            print("Tenth file=", fname10)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname10:
                break
            else:
                i += 1


        else:
            return

    if not fname1:                                  # if user enters return, then we will exit the loop
        return
    else:                                           # Otherwise we run the histogram which will print the complete statistics
        hstgrm(fname1)

    if not fname2:
        return
    else:
        hstgrm(fname2)

    if not fname3:
        return
    else:
        hstgrm(fname3)

    if not fname4:
        return
    else:
        hstgrm(fname4)

    if not fname5:
        return
    else:
        hstgrm(fname5)

    if not fname6:
        return
    else:
        hstgrm(fname6)

    if not fname7:
        return
    else:
        hstgrm(fname7)

    if not fname8:
        return
    else:
        hstgrm(fname8)

    if not fname9:
        return
    else:
        hstgrm(fname9)

    if not fname10:
        return
    else:
        hstgrm(fname10)

def hstgrm(fname):
    hist_words = {}                        # initializing all the dictionaires
    hist_char = {}
    hist_bi = {}
    hist_tri = {}
    biwd = []                               # initializing the lists for biwords and triwords
    triwd = []
    tot_word = 0                            # initializing counters for each file
    tot_char = 0
    tot_bi   = 0
    tot_tri = 0
    global comb_tot_word                    # calls back global variable which will accumulate count for all files
    global comb_tot_char
    global comb_tot_bi
    global comb_tot_tri

    fopen = open(fname)                     # This will open one file at a time, and fname is passed as an argument
    for line in fopen:                      # iterative loop to read each line

        line=line.lower().replace(".","").replace('--',"").replace('-',"").replace('"',"").replace(",","").replace("'","").replace("!","").replace(";","").replace(":","").replace("?","").strip()
        #print(line)
        # Conditions are met to make sure we only count the lower case letters.
        line=line.split()                   # split the line into a list of words
        for word in line:                   # for loop to iterate through each word in the line
            if word.isalpha():              # checks if word is alpha
                tot_word += 1               # increments total word counter statistics for each file
                comb_tot_word += 1          # increments combined total word counter for cumulative statistics of all files of an author
                hist_words[word] = hist_words.get(word,0) + 1   #increments and update hist_words dictionary with key as words and value as frequency
                comb_hist_words[word] = comb_hist_words.get(word,0) + 1 # same as above but keeps updating the cumulative combined histogram of words for all files

                for c in word:              # iterates through each character in the word
                    if c.isalpha():         # does the loop for character as it is done above for words
                        tot_char += 1
                        comb_tot_char += 1
                        hist_char[c] = hist_char.get(c,0) + 1
                        comb_hist_char[c] = comb_hist_char.get(c,0) + 1



            for i in range(len(word)-1):    # for loop to generate a list biwd (biagrams)for all words in a line
                biwd.append(word[i:i+2])    # appends every biwd to the list
            if len(word)>1:                 # incase we have a single character(cannot form biword) do not accumulate counter
                tot_bi += len(word)-1       # update biword counter for each file iterated through all words and all lines
                comb_tot_bi += len(word)-1  # does same as above for cumulative counter for biword without reseting count for previous fie
                #print(tot_bi)                                                  # test print statements

            for j in range(len(word)-2):    # loop to generate a list triwd (trigrams) for all words in line
                triwd.append(word[j:j+3])   # same as above
            if len(word)>2:                 # if word has more than 2 characters then update counters as above for bigrams
                tot_tri += len(word)-2
                comb_tot_tri += len(word)-2
                #print(tot_tri)                                                 # test print statements

    for bich in biwd:                       # loop through each bigram in the list biwd
        hist_bi[bich] = hist_bi.get(bich,0) + 1     # update the dictionary for bigrams(hist_bi) with key as bigram and value as frequency
        comb_hist_bi[bich] = comb_hist_bi.get(bich,0) + 1   #same as above for cumulative

    for trich in triwd:                     # loop throguh each trigram in the list triwd
        hist_tri[trich] = hist_tri.get(trich,0) + 1 # as above for bigram
        comb_hist_tri[trich] = comb_hist_tri.get(trich,0) + 1


    print("")
    print("Statistics for :", fname)
    print("-------------------------------------------------------------")
    print("Letter Frequencies:")
    list_char=[]                                                # create a list_xxxx to read the dictionary(hist_xxxx)
    for key_char, value_char in hist_char.items():              # iterates through key and value for each items in the dicionary
        list_char.append((value_char,key_char))                 # appends the list by swapping value and key
    list_char.sort(reverse=True)                                # sorts the list in reverse order (highest frequency on top)
    for value_char, key_char in list_char[:26]:                 # iterates through list_xxxx and prints the top 26 items
        print('{:20s}'.format(key_char), '{:1d}'.format(value_char), '({:.3f}%)' .format(value_char/tot_char*100)) # prints the key(Word) and value(frequency) and percentage in proper format

    print("")
    print("Word Frequencies:")
    list_word=[]
    for key_word, value_word in hist_words.items():
        list_word.append((value_word,key_word))
    list_word.sort(reverse=True)
    for value_word, key_word in list_word[:25]:
        print('{:20s}'.format(key_word), '{:6d}'.format(value_word), '({:.3f}%)' .format(value_word/tot_word*100))

    print("")
    print("Bigram Frequencies:")
    list_biag=[]
    for key_bi, value_bi in hist_bi.items():
        list_biag.append((value_bi,key_bi))
    list_biag.sort(reverse=True)
    for value_bi, key_bi in list_biag[:25]:
        print('{:20s}'.format(key_bi), '{:6d}'.format(value_bi), '({:.3f}%)' .format(value_bi/tot_bi*100))

    print("")
    print("Trigram Frequencies:")
    list_triag=[]
    for key_tri, value_tri in hist_tri.items():
        list_triag.append((value_tri,key_tri))
    list_triag.sort(reverse=True)
    for value_tri, key_tri in list_triag[:25]:
        print('{:20s}'.format(key_tri), '{:6d}'.format(value_tri), '({:.3f}%)' .format(value_tri/tot_tri*100))



    print("")
    print("Cumulative Statistics as of this step:")
    print("---------------------------------------")
    print("")
    print("Cumulative Letter Frequencies:")
    list_char=[]
    for key_char, value_char in comb_hist_char.items():                 # same as above but does for cumulative statistics
        list_char.append((value_char,key_char))
    list_char.sort(reverse=True)
    for value_char, key_char in list_char[:26]:
        print('{:20s}'.format(key_char), '{:6d}'.format(value_char), '({:.3f}%)' .format(value_char/comb_tot_char*100))

    print("")
    print("Cumulative Word Frequencies:")
    list_word=[]
    for key_word, value_word in comb_hist_words.items():
        list_word.append((value_word,key_word))
    list_word.sort(reverse=True)
    for value_word, key_word in list_word[:25]:
        print('{:20s}'.format(key_word), '{:6d}'.format(value_word), '({:.3f}%)' .format(value_word/comb_tot_word*100))

    print("")
    print("Cumulative Bigram Frequencies:")
    list_biag=[]
    for key_bi, value_bi in comb_hist_bi.items():
        list_biag.append((value_bi,key_bi))
    list_biag.sort(reverse=True)
    for value_bi, key_bi in list_biag[:25]:
        print('{:20s}'.format(key_bi), '{:6d}'.format(value_bi), '({:.3f}%)' .format(value_bi/comb_tot_bi*100))

    print("")
    print("Cumulative Trigram Frequencies:")
    list_triag=[]
    for key_tri, value_tri in comb_hist_tri.items():
        list_triag.append((value_tri,key_tri))
    list_triag.sort(reverse=True)
    for value_tri, key_tri in list_triag[:25]:
        print('{:20s}'.format(key_tri), '{:6d}'.format(value_tri), '({:.3f}%)' .format(value_tri/comb_tot_tri*100))

    return()

allfile()
