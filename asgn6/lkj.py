#!/usr/bin/python3
# coding=utf-8
#
# Assignment 6
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu


import os.path                             # will return true if the file exists (found on course web page)
comb_hist_words = {}
comb_hist_char = {}
comb_hist_bi = {}
comb_hist_tri = {}
comb_tot_word = 0
comb_tot_char = 0
comb_tot_bi   = 0
comb_tot_tri = 0

comb_list_words =[]
comb_list_char =[]
comb_list_bi =[]
comb_list_tri =[]

def openfile():                            # function that opens file

    aval = False
    while not aval:
        filename = input("What file do you want to import? ", )         # user input for files being opened, stored into variable
        aval = os.path.isfile(filename)                                 # will make sure the file entered exists
        if aval:
            #print("Your file,", filename, "is available: ")
            #print ("")
            return filename
        if len(filename)<1:
            break
        elif not aval:
            print("I don't recognize the file,", filename, "Try Again!!!")

            print("")

    return

def allfile():
    i=1
    fname1=""
    fname2=""
    fname3=""
    fname4=""
    fname5=""
    fname6=""
    fname7=""
    fname8=""
    fname9=""
    fname10=""
    #numfile = input("How many files? ", )
    while i <= 10:
        if i == 1:
            fname1 = openfile()
            print("First file is: ", fname1)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")

            if not fname1:
                break
            else:
                i=i+1

        elif i == 2:
            fname2 = openfile()
            print("Second file=", fname2)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname2:
                break
            else:
                i=i+1

        elif i == 3:
            fname3 = openfile()
            print("Third file=", fname3)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname3:
                break
            else:
                i=i+1

        elif i == 4:
            fname4 = openfile()
            print("Fourth file=", fname4)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname4:
                break
            else:
                i = i+1

        elif i == 5:
            fname5 = openfile()
            print("Fifth file=", fname5)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname5:
                break
            else:
                i = i+1

        elif i == 6:
            fname6 = openfile()
            print("Sixth file=", fname6)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname6:
                break
            else:
                i = i+1

        elif i == 7:
            fname7 = openfile()
            print("Seventh file=", fname7)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname7:
                break
            else:
                i = i+1

        elif i == 8:
            fname8 = openfile()
            print("Eighth file=", fname8)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname8:
                break
            else:
                i = i+1

        elif i == 9:
            fname9 = openfile()
            print("Ninth file=", fname9)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname9:
                break
            else:
                i = i+1

        elif i == 10:
            fname10 = openfile()
            print("Tenth file=", fname10)
            print("PRESS ENTER WHEN DONE ENTERING FILES")
            print("")
            if not fname10:
                break
            else:
                i = i+1


        else:
            return

    if not fname1:
        return
    else:
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
    hist_words = {}                        # initializing all the files
    hist_char = {}
    hist_bi = {}
    hist_tri = {}
    biwd = []
    triwd = []
    tot_word = 0
    tot_char = 0
    tot_bi   = 0
    tot_tri = 0
    global comb_tot_word
    global comb_tot_char
    global comb_tot_bi
    global comb_tot_tri

    fopen = open(fname)
    for line in fopen:

        line=line.lower().replace(".","").replace('--',"").replace('-',"").replace('"',"").replace(",","").replace("'","").replace("!","").replace(";","").replace(":","").replace("?","").strip()
        #print(line)
        line=line.split()
        for word in line:
            if word.isalpha():
                tot_word += 1
                comb_tot_word += 1
                hist_words[word] = hist_words.get(word,0) + 1
                comb_hist_words[word] = comb_hist_words.get(word,0) + 1

                for c in word:
                    if c.isalpha():
                        tot_char += 1
                        comb_tot_char += 1
                        hist_char[c] = hist_char.get(c,0) + 1
                        comb_hist_char[c] = comb_hist_char.get(c,0) + 1



            for i in range(len(word)-1):
                biwd.append(word[i:i+2])
            if len(word)>1:
                tot_bi += len(word)-1
                comb_tot_bi += len(word)-1
                #print(tot_bi)

            for j in range(len(word)-2):
                triwd.append(word[j:j+3])
            if len(word)>2:
                tot_tri += len(word)-2
                comb_tot_tri += len(word)-2
                #print(tot_tri)

    for bich in biwd:
        hist_bi[bich] = hist_bi.get(bich,0) + 1
        comb_hist_bi[bich] = comb_hist_bi.get(bich,0) + 1

    for trich in triwd:
        hist_tri[trich] = hist_tri.get(trich,0) + 1
        comb_hist_tri[trich] = comb_hist_tri.get(trich,0) + 1


    print("")
    print("Letter Frequencies:")
    list_char=[]
    for key_char, value_char in hist_char.items():
        list_char.append((value_char,key_char))
    list_char.sort(reverse=True)
    for value_char, key_char in list_char[:26]:
        print('{:20s}'.format(key_char), '{:6d}'.format(value_char), '({:.3f}%)' .format(value_char/tot_char*100))

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

    return()




allfile()
