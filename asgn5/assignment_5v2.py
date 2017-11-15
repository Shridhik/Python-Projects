#!/usr/bin/python3
# coding=utf-8
#
# Assignment 5
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu


def filelist():                                                         # function that opens the user input file, and reads it, and turns it all lower case
    file1 = open(input("What text file would you like to import?"))     # opens file
    line1 = (file1.read())                                              # reads the file
    line1 = line1.lower()                                               # turns all letters lowercase
    #print(line1)                                                       # previously used print statement
    return line1                                                        # returns the information down

l1 = filelist()                                                         # stores the function call into variable l1


def clean(l1):                                                          # function that cleans words leaving only integers and letters
    l2=[]                                                               # empty list to store new cleaned list words in
    listofwords = l1.strip().split()                                    # list of words are now put into a list, knows as list of words, and have whitespace removed
    s = len(listofwords)                                                # s will hold the length of how many elements are in the list
    #print(s)
    for i in range(s):                                                  # for every element in the list of words
        #print(i)
        clean_s = ""                                                    # blank string to keep cleaned words in
        for c in listofwords[i]:                                        # goes through each letter of each word
             if c.isalpha() or c.isalnum():                             # checks to make sure only numbers and letter go through
                clean_s = clean_s + c
        #print(clean_s)
        if clean_s != "":                                               # makes you we dont include blank strings that may have once contained unreadable characters
            l2.append(clean_s)                                          # adds clean strings to List 2
    #print(l2)                                                           # prints l2
    return l2

cleanlist = clean(l1)


def sort_cl(cleanlist):                                                 # function to sort out the words without using the s
    n = len(cleanlist)
    for i in range(n):                                                  # https://en.wikipedia.org/wiki/Bubble_sort is a method i found when googling sort methods
         for j in range(n-1):                                            # For loop to cover all elements in the list
             if cleanlist[j] > cleanlist[j+1]:                           # if the proceeding element is less than the element before it, I will swap the two elements
                 (cleanlist[j],cleanlist[j+1]) = (cleanlist[j+1],cleanlist[j]) # swaps the two elements if above condition is met

    print(cleanlist)
    return cleanlist                                                    # returns alphabatized word list

alplist = sort_cl(cleanlist)                                            # holds the return value in variable alp list which is the alphabatized list


def count(alplist):                                                     # function to count the amount of times each word is said
    l3 = []                                                             # empty list that stores new words without repetition
    frq = []                                                            # empty list that will contain how often a word occurs
    for e in alplist:                                                   # for every element in all the words
        if e not in l3:                                                 # if the word is not already repeated, it will be stored in L3
            l3.append(e)
            frq.append(1)
        else:                                                           # if it is repeated, and in l3, the element will have its location in the list recorded
            loc = l3.index(e)
            frq[loc] = frq[loc] + 1                                     # the location of the frequency will raise by 1
    #print(l3)
    #print(frq)

    n = len(l3)
    for i in range(n):                                                  # prints both the results side by sode
        print(frq[i], l3[i])

count(alplist)                                                          # runs everything



