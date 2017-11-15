#!/usr/bin/python3
#
# Assignment 3
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu

import random


def strt():                                                                 # function to return  user input for start value
    start = -1                                                              # initializing variable to run the while loop
    while int(start) < 1 or int(start) > 499:                               # contingency for valid user inputs
        start = input("What is your start location? (between 1 and 499) ")  # user input assigned to variable start
    return int(start)                                                       # returns user input assigned to start


def mini(x):                                                                                # function to return user input for minimum value
    mn = -1                                                                                 # initializing variable to run the while loop
    while int(mn) < 0 or int(mn) > int(x) - 1:                                              # contingency for valid user inputs
        mn = input("What is your minimum value? (between 0 and " + str(int(x) - 1) + ") ")  # user input is assigned to variable mn
    return int(mn)                                                                          # returns user input mn


def maxi(y):                                                                                 # function to return maximum number
    mx = -1                                                                                  # initializing the variable to run the while loop
    while int(mx) < (int(y) + 1) or int(mx) > 500:                                           # contingency for the valid parameters
        mx = input("What is your maximum value? (between " + str(int(y) + 1) + " and 500) ") # user input is assigned into mx
    return int(mx)                                                                           # returns user input mx


def rhtprcnt():                                                                          # function to return percentage chance of moving right
    rp = 0                                                                               # initializing the variable to run the while loop
    while int(rp) < 1 or int(rp) > 99:                                                   # contingency for valid parameters
        rp = input("What is the percentage chance of moving right? (between 1 and 99) ") # user input is stored into rp
    return int(rp)                                                                            # returns the user input rp


def wlks():                                                         # function to return number of walks done
    n_walks = -1                                                    # initializing the variable to run the while loops
    while int(n_walks) < 0 or int(n_walks) > 10000:                 # contingency for valid parameters
        n_walks = input("How many walks? (between 0 and 10000) ")   # user input is stored into n_walks
    return int(n_walks)                                                  # returns the user input n_walks


ST = strt()     #runs function strt(), and stores return value in variable ST
MN = mini(ST)   #variable ST is passed to function mini() since we need to know the start value
MX = maxi(ST)   #variable ST is passed to function maxi() since we need the start value agaim
RH = rhtprcnt() #runs the rhtprcnt() function and stores the return value into variable RH
WK = wlks()     #runs the wlks() function and stores the return value into variable WK


def direction():                        # function to randomly select direction (left/right) for random walk
    outcome = ["left", "right"]         # the result can go either left or right
    direct = random.choice(outcome)     # I found the function random.choice in the python textbook
    #print(direct)
    return direct                       # returns the value of random direction


def one_step(RH):                       # function to find if we move left(-1) or right(+1) based on random percentage
    rnd = 0
    #dr = direction()
    rnd = random.random() * 100         # using builtin random num generation and convert to percentage
    #print("RND = ",rnd)
    if rnd > RH:                        # compare random percentage to rhtprcent(user input) to determine left(-1 step) or right ( + 1 step)
    #if dr == "left":
        x = -1
    else:
        x = +1
    print(x)
    return x                            # returns x(+1 if right) and (-1 if left)


def one_walk_steps(ST,MN,MX,RH):
    location = ST
    i = 0
    result = 0
    while location < MX and location > MN and i < 5001:
        x = one_step(RH)
        location = location + x
        print(location)

        # if i == 5000:
        #    return i
        # else:
        if location == MX:
            result = i * 1
        elif location == MN:
            result = i * -1
        elif i == 5000:
            result = 5000

        i = i + 1
        #print(result)
    return result


def mul_walk(WK):
    j = 0
    hit_min = 0
    hit_max = 0
    hit_5000 = 0
    while j < WK:
        ows= one_walk_steps(ST,MN,MX,RH)
        print("OWS =", ows)
        if ows < 0:
            hit_min = hit_min + 1
            print("HIT_MIN =" , hit_min)
            j=j+1

        elif ows == 5000:
            hit_5000 = hit_5000 + 1
            print("HIT_5000 =" , hit_5000)
            j=j+1

        elif ows > 0:
            hit_max = hit_max + 1
            print("HIT_MAX =" , hit_max)
            j=j+1

    print("number of walks that ended on the left:", )
    print("     Number of walks: ", hit_min)

    print("Number of walks that ended on the right:" )
    print("     Number of walks: ", hit_max)

    print("Nuber of walks that hit 5000 steps:")
    print("     Number of walks: ", hit_5000)

mul_walk(WK)
