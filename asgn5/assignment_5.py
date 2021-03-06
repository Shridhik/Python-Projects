#!/usr/bin/python3
# coding=utf-8
#
# Assignment 5
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu


def fileopen():                                                         # function that opens the user input file, and reads it, and turns it all lower case
    file1 = open(input("What text file would you like to import?"))     # opens file
    line1 = (file1.read())                                              # reads the file
    line1 = line1.lower()                                               # turns all letters lowercase
    return line1                                                        # returns the information down

l1 = fileopen()                                                         # stores the function call into variable l1


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

to_sort = clean(l1)


#def sort_cl(cleanlist):                                                 # function to sort out the words without using the s
#    n = len(cleanlist)
#    for i in range(n):                                                  # https://en.wikipedia.org/wiki/Bubble_sort is a method i found when googling sort methods
#        for j in range(n-1):                                            # For loop to cover all elements in the list
#            if cleanlist[j] > cleanlist[j+1]:                           # if the proceeding element is less than the element before it, I will swap the two elements
#                (cleanlist[j],cleanlist[j+1]) = (cleanlist[j+1],cleanlist[j]) # swaps the two elements if above condition is met

#    #print(cleanlist)
#    return cleanlist                                                    # returns alphabatized word list


def sort_cl(to_sort):
    A = to_sort[:]
    B = []
    A.append(False)
    B.append(False)
    print(A)
    print(B)
    prev = 'z' * 100
    last = 'A_list'                                 # initialized the last appended list as A
    while True:                                     # indefinite loop using while statement
        if A[0] is not False and B[0] is False:     # If exactly one value is False choose the other value
            if A[0] >= prev:                        # If exactly one value is larger than or equal to the previous value, choose it
                prev = A[0]                         # assign previous value to the front of list
                if last == 'A_list':                # if last appended list is A
                    A.append(A[0])                  # append A[i] behind previous value
                    del A[0]                        # delete first element in list A
                elif last == 'B_list':              # if last list to be append is B
                    last = 'A_list'                 # assigns last list append list as A
                    A.append(A[0])                  # append A[i] behind previous value
                    del A[0]                        # delete first element in list A
            elif A[0] < prev:                       # if A[i] is less than previous value it will be appended to the other list
                prev = A[0]                         # sets the previous value equal to the current value of A[i] for the next run through
                if last == 'B_list':                # if last list to be append is 'b'
                    last = 'A_list'                 # assigns the last list to be append to 'a'
                    A.append(A[0])                  # append A[i] to the end of the list A
                    del A[0]                        # deleted element 0 of list A
                elif last == 'A_list':              # if last appended element is A
                    last = 'B_list'                 # assign last appended list as B
                    B.append(A[0])                  # append the element A[i] to B
                    del A[0]                        # delete element 0 of list A
        elif A[0] is False and B[0] is not False:   # this is for when A[0] is false but B[0] isn't false
            if B[0] >= prev:
                prev = B[0]
                if last == 'A_list':
                    A.append(B[0])
                    del B[0]
                elif last == 'B_list':
                    B.append(B[0])
                    del B[0]
            elif B[0] < prev:
                prev = B[0]
                if last == 'B_list':
                    last = 'A_list'
                    A.append(B[0])
                    del B[0]
                elif last == 'A_list':
                    last = 'B_list'
                    B.append(B[0])
                    del B[0]
        elif A[0] is not False and B[0] is not False:     #this is for when neither A nor B are false
            if A[0] >= prev and B[0] >= prev:
                if A[0] >= B[0]:
                    prev = B[0]
                    if last == 'A_list':
                        A.append(B[0])
                        del B[0]
                    elif last == 'B_list':
                        B.append(B[0])
                        del B[0]
                elif A[0] < B[0]:
                    prev = A[0]
                    if last == 'A_list':
                        A.append(A[0])
                        del A[0]
                    elif last == 'B_list':
                        B.append(A[0])
                        del A[0]
            elif A[0] >= prev > B[0]:
                prev = A[0]
                if last == 'A_list':
                    A.append(A[0])
                    del A[0]
                elif last == 'B_list':
                    B.append(B[0])
                    del B[0]
            elif A[0] < prev <= B[0]:
                prev = B[0]
                if last == 'A_list':
                    A.append(B[0])
                    del B[0]
                elif last == 'B_list':
                    B.append(B[0])
                    del B[0]
            elif A[0] < prev and B[0] < prev:
                if A[0] >= B[0]:
                    prev = B[0]
                    if last == 'A_list':
                        last = 'B_list'
                        B.append(B[0])
                        del B[0]
                    elif last == 'B_list':
                        last = 'A_list'
                        A.append(B[0])
                        del B[0]
                elif A[0] < B[0]:
                    prev = A[0]
                    if last == 'A_list':
                        last = 'B_list'
                        B.append(A[0])
                        del A[0]
                    elif last == 'B_list':
                        last = 'A_list'
                        A.append(A[0])
                        del A[0]

#        elif A[0] is False and B[0] is False and len(A) == 1:
#            del A[0]
#            del B[0]
#            return B
        elif A[0] is False and B[0] is False and len(B) == 1:
            del A[0]
            del B[0]
            return A
        elif A[0] == False and B[0] == False and len(A) > 1 and len(B) > 1:
            A.append(False)
            B.append(False)
            del A[0]
            del B[0]
         #   prev = 'z' * 100
            prev = B[0]

alplist = sort_cl(to_sort)                                            # holds the return value in variable alp list which is the alphabatized list

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




