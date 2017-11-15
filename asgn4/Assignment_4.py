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
        instr = instr.strip()                   # removes white space her side of the input string (as taught in class)
        print(instr)                            # prints user input for user to see
        return instr                            # returns value of user input for further use
    else:                                       # recursion in case the conditions for user input or not met
        inpstr()                                # loops back to the function
    return instr                                # returns value of instr for further use


ig = inpstr()


def keystr():                                   # function to get user input of keystring
    ky = input("What is your key: ")
    if len(ky) >= 1:
        ky = ky.upper()
        ky = ky.strip()
        ky = ky.replace(" ", "")                 # Citation: Learnt string replace in https://docs.python.org/3/library/stdtypes.html
        for i in range(10):
            ky = ky.replace(str(i), "")         # replaces  numbers with no space
        print(ky)
        return ky
    else:
        keystr()                                # User recursion in case the condition of len(ky) >= 1 is not met

    return ky

key = keystr()                                  # stores the return value of keystring in variable key to be used later


def edopt(ig, key):                              # function to request user the option of inputing either e or d
    ed = input("(E)ncrypt or (D)ecrypt? ")      # request user input to decide to encrypt or decrypt
    ed = ed.strip()                             # strips white space on both sides
    ed = ed.replace(" ", "")                     # replaces any white space in between
    ed = ed.upper()                             # changes string to uppercase
    if len(ed) >= 1 and ed == "E" or ed == "D" or ed == "ENCRYPT" or ed == "DECRYPT":   # a list of all of the acceptable conditions
        if ed[0] == "E":                        # condition true if E,e,encrypt,Encrypt is used
            print(ed[0])                        # prints first character
            encrypt(ig, key)                     # runs encrypt function
            return
        elif ed[0] == "D":                      # condition true if D,d,decrypt,Decrypt is used
            print(ed[0])
            decrypt(ig, key)                     # runs decrypt function
            return
        return
    else:
        edopt(ig, key)                           # otherwise recursion to edopt function
    return ed                                   # returns value of the option


def encrypt(ig, key):

    enchr = ""

    ig = ig.replace(" ", "")                 # Googled how to replace white space in the middle of a string on googlehttps://docs.python.org/3/library/stdtypes.html
    for i in range(10):                     # i goes to any number from 0 - 9
        ig = ig.replace(str(i), "")          # removes any number between 0 - 9
    print(ig)                               # prints user input for user to see

    if len(ig) > len(key):                  # condition is true if the length of message string is greater than keyword
        nkey = len(ig)/len(key)             # stores the value of how many times we should repeat the word into variable nkey
        nkey = int(nkey)                    # converts nkey to an integer
        # print(nkey)
        rkey = len(ig) % len(key)             # variable that store the modulo
        # print(rkey)
        key = key * nkey                    # multiples keyword with repetition of word
        key = key + key[:rkey]              # ads the modulo (remainding letters of key) to the value of ky
        print(key)

    elif len(ig) < len(key):                # condition is true if length of message string is less than the length of the key word
        key = key[:len(ig)]                 # key is truncated to math the length of user message
        print(key)

    else:                                   # condition is true if message and key length are same
        print(key)                          # prints key
    space = ""
    for i in range(len(ig)):                # loop to run as long as the length of input message
        msgnum = ord(ig[i])-ord("A")        # converts each character of message to number
        keynum = ord(key[i])-ord("A")       # converts each character of key to number
        cumnum = msgnum + keynum            # adds both the message and key numbers
        cumnum = cumnum % 26                # if above 26 calculates the modulo
        enchr = enchr + chr(cumnum + ord("A"))  # converts number to character and updates the output message
        if i == 7 or i == 15 or i == 23 or i == 31 or i == 39 or i == 47 or i == 55:  # adds space after 8th character
            enchr = enchr + " "
    print(enchr)                            # prints the encrypted output
    return enchr                            # returns encoded output


def decrypt(ig, key):
    dechr = ""

    igs = ig.replace(" ", "")            # Googled how to replace white space in the middle of a string on googlehttps://docs.python.org/3/library/stdtypes.html
    for i in range(10):                 # for loop ranges from 0 - 9
        igs = igs.replace(str(i), "")    # removes any number between 0 - 9
    print(igs)                          # prints user input for user to see

    if len(igs) > len(key):             # condition is true if the length of message string is greater than keyword
        nkey = len(igs)/len(key)        # stores the value of how many times we should repeat the word into variable nkey
        nkey = int(nkey)                # converts nkey to an integer
        rkey = len(igs) % len(key)        # variable that store the modulo
        key = key * nkey                # multiples keyword with repetition of word
        key = key + key[:rkey]          # ads the modulo (remainding letters of key) to the value of ky
        print(key)

    elif len(igs) < len(key):           # condition is true if length of message string is less than the length of the key word
        key = key[:len(igs)]            # key is truncated to match the length of user message
        print(key)

    else:
        print(key)                      # prints the key

    for i in range(len(igs)):           # loop to run as long as input message
        msgnum = ord(igs[i])-ord("A")   # converts each character of input message to number
        keynum = ord(key[i])-ord("A")   # converts each character of key to number
        cumnum = msgnum - keynum        # subtracts to reverse encoded information
        cumnum = cumnum % 26            # calculate modulo to reset if more than 26
        dechr = dechr + chr(cumnum + ord("A"))  # converts number to character

    print(dechr)                        # prints decoded string without any numbers and space

#    pos1 = ig.find(" ")                 # finds the first space position
#    pos2 = ig.rfind(" ")                # finds the last space position
#    alp = ig[pos1:pos2+1]               # slices the character from first space to last space position
#    dechr = dechr[:pos1]+alp+dechr[pos1:]   # adds the slice to the decoded
#    print(dechr)                        # prints the decoded string with the slice
    poss = 0
    for j in range(len(ig)):            # goes through each character the the original input
            if ig[j] == "*":            # finds the number, one at a time, and if it finds the specific number:
                posx = ig.find("*")     # we assign position x as the location in which this number is
                dechr = dechr[:posx]+"*"+dechr[posx:]   #adds the number back into the decrypted code
            elif ig[j] == "0":
                pos0 = ig.find("0")
                dechr = dechr[:pos0]+"0"+dechr[pos0:]
            elif ig[j] == "1":
                pos1 = ig.find("1")
                dechr = dechr[:pos1]+"1"+dechr[pos1:]
            elif ig[j] == "2":
                pos2 = ig.find("2")
                dechr = dechr[:pos2]+"2"+dechr[pos2:]
            elif ig[j] == "3":
                pos3 = ig.find("3")
                dechr = dechr[:pos3]+"3"+dechr[pos3:]
            elif ig[j] == "4":
                pos4 = ig.find("4")
                dechr = dechr[:pos4]+"4"+dechr[pos4:]
            elif ig[j] == "5":
                pos5 = ig.find("5")
                dechr = dechr[:pos5]+"5"+dechr[pos5:]
            elif ig[j] == "6":
                pos6 = ig.find("6")
                dechr = dechr[:pos6]+"6"+dechr[pos6:]
            elif ig[j] == "7":
                pos7 = ig.find("7")
                dechr = dechr[:pos7]+"7"+dechr[pos7:]
            elif ig[j] == "8":
                pos8 = ig.find("8")
                dechr = dechr[:pos8]+"8"+dechr[pos8:]
            elif ig[j] == "9":
                pos9 = ig.find("9")
                dechr = dechr[:pos9]+"9"+dechr[pos9:]
            elif ig[j] == ' ':
                poss = ig.find(' ')
                dechr = dechr[:poss] + " " + dechr[poss:]
            else:
                dechr = dechr
    print(dechr)
    return dechr                        # returns the decoded string


edopt(ig, key)
