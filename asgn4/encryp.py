#!/usr/bin/python3
# coding=utf-8
#
# Assignment 3
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu


def inpstr():                                   # function to get user input message
    instr = input("What is your message: ")     # assigns user input into variable instr (insputstring)
    if len(instr) >= 1:                         # this condition is true if input is more than one character
        instr = instr.upper()                   # converts input to upper case
        instr = instr.strip()                   # removes white space on either side of the input string (as taught in class)
        #instr = instr.replace(" ","")           # Googled how to replace white space in the middle of a string on googlehttps://docs.python.org/3/library/stdtypes.html
        #for i in range(10):                     # i goes to any number from 0 - 9
        #    instr = instr.replace(str(i),"")    # removes any number between 0 - 9
        print(instr)                            # prints user input for user to see
        return instr                            # returns value of user input for further use
    else:                                       # recursion in case the conditions for user input or not met
        inpstr()                                # loops back to the function
    return instr                                # returns value of instr for further use


ig = inpstr()

def keystr():                                   # function to get user input of keystring
    #ig = inpstr()
    nkey = 0                                    #initializes variables
    rkey = 0
    ky = input("What is your key: ")
    if len(ky) >= 1:
        ky = ky.upper()
        ky = ky.strip()
        ky = ky.replace(" ","")           #https://docs.python.org/3/library/stdtypes.html
        for i in range(10):
            ky = ky.replace(str(i),"")
        print(ky)
        return ky

    else:
        keystr()                          # User recursion in case the condition of len(ky) >= 1 is not met

    return ky

key = keystr()


def edopt(ig,key):                            # function to request user the option of inputing either e or d
    ed = input("(E)ncrypt or (D)ecrypt? ")
    ed = ed.strip()
    ed = ed.replace(" ","")
    ed = ed.upper()
    if len(ed) >= 1 and ed == "E" or ed == "D" or ed == "ENCRYPT" or ed == "DECRYPT":   # a list of all of the acceptable conditions
        if ed[0] == "E":
            print(ed[0])
            encrypt(ig,key)
            return
        elif ed[0] == "D":
            print("I am here")
            decrypt(ig,key)
            return
        return
    else:
        edopt(ig,key)
    return ed




def encrypt(ig,key):
    msgnum = 0
    keynum = 0
    cumnum = 0
    nkey = 0
    rkey = 0
    enchr=""

    ig = ig.replace(" ","")           # Googled how to replace white space in the middle of a string on googlehttps://docs.python.org/3/library/stdtypes.html
    for i in range(10):                     # i goes to any number from 0 - 9
        ig = ig.replace(str(i),"")    # removes any number between 0 - 9
    print(ig)                            # prints user input for user to see

    if len(ig) > len(key):             # condition is true if the length of message string is greater than keyword
        nkey = len(ig)/len(key)        # stores the value of how many times we should repeat the word into variable nkey
        nkey = int(nkey)              # converts nkey to an integer
        #print(nkey)
        rkey = len(ig)%len(key)        # variable that store the modulo
        #print(rkey)
        key = key * nkey                # multiples keyword with repetition of word
        key = key + key[:rkey]           # ads the modulo (remainding letters of key) to the value of ky
        print(key)

    elif len(ig) < len(key):           # condition is true if length of message string is less than the length of the key word
        key = key[:len(ig)]             # key is truncated to math the length of user message
        print(key)

    else:
        print(key)

    for i in range(len(ig)):
        msgnum = ord(ig[i])-ord("A")
        keynum = ord(key[i])-ord("A")
        cumnum = msgnum + keynum
        cumnum = cumnum % 26
        enchr  = enchr + chr(cumnum + ord("A"))
        if i == 7:
            enchr = enchr + " "
    print(enchr)
    return




def decrypt(ig,key):
    msgnum = 0
    keynum = 0
    cumnum = 0
    nkey = 0
    rkey = 0
    enchr=""
    igd=""

    igs = ig.replace(" ","")           # Googled how to replace white space in the middle of a string on googlehttps://docs.python.org/3/library/stdtypes.html
    for i in range(10):                     # i goes to any number from 0 - 9
        igs = igs.replace(str(i),"")    # removes any number between 0 - 9
    print(igs)                            # prints user input for user to see

                          # prints user input for user to see

    if len(igs) > len(key):             # condition is true if the length of message string is greater than keyword
        nkey = len(igs)/len(key)        # stores the value of how many times we should repeat the word into variable nkey
        nkey = int(nkey)              # converts nkey to an integer
        #print(nkey)
        rkey = len(igs)%len(key)        # variable that store the modulo
        #print(rkey)
        key = key * nkey                # multiples keyword with repetition of word
        key = key + key[:rkey]           # ads the modulo (remainding letters of key) to the value of ky
        print(key)

    elif len(igs) < len(key):           # condition is true if length of message string is less than the length of the key word
        key = key[:len(igs)]             # key is truncated to math the length of user message
        print(key)

    else:
        print(key)


    print(key)
    for i in range(len(igs)):
        msgnum = ord(igs[i])-ord("A")
        keynum = ord(key[i])-ord("A")
        cumnum = msgnum - keynum
        cumnum = cumnum % 26
        enchr  = enchr + chr(cumnum + ord("A"))

    print(enchr)
    return




edopt(ig,key)




