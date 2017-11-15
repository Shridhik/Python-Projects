#!/usr/bin/python3
# coding=utf-8
#
# Assignment 3
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu

import random


def strt():  # function to return  user input for start value
    start = -1  # initializing variable to run the while loop
    while int(start) < 1 or int(start) > 499:  # contingency for valid user inputs
        start = input("What is your start location? (between 1 and 499) ")  # user input assigned to variable start
    return int(start)  # returns user input assigned to start


def mini(x):  # function to return user input for minimum value
    mn = -1  # initializing variable to run the while loop
    while int(mn) < 0 or int(mn) > int(x) - 1:  # contingency for valid user inputs
        mn = input("What is your minimum value? (between 0 and " + str(int(x) - 1) + ") ")  # user input is assigned to variable mn
    return int(mn)  # returns user input mn


def maxi(y):  # function to return maximum number
    mx = -1  # initializing the variable to run the while loop
    while int(mx) < (int(y) + 1) or int(mx) > 500:  # contingency for the valid parameters
        mx = input(
            "What is your maximum value? (between " + str(int(y) + 1) + " and 500) ")  # user input is assigned into mx
    return int(mx)  # returns user input mx


def rhtprcnt():  # function to return percentage chance of moving right
    rp = 0  # initializing the variable to run the while loop
    while int(rp) < 1 or int(rp) > 99:  # contingency for valid parameters
        rp = input("What is the percentage chance of moving right? (between 1 and 99) ")  # user input is stored into rp
    return int(rp)  # returns the user input rp


def wlks():  # function to return number of walks done
    n_walks = -1  # initializing the variable to run the while loops
    while int(n_walks) < 0 or int(n_walks) > 10000:  # contingency for valid parameters
        n_walks = input("How many walks? (between 0 and 10000) ")  # user input is stored into n_walks
    return int(n_walks)  # returns the user input n_walks


ST = strt()  # runs function strt(), and stores return value in variable ST
MN = mini(ST)  # variable ST is passed to function mini() since we need to know the start value
MX = maxi(ST)  # variable ST is passed to function maxi() since we need the start value agaim
RH = rhtprcnt()  # runs the rhtprcnt() function and stores the return value into variable RH
WK = wlks()  # runs the wlks() function and stores the return value into variable WK


def one_step(RH):                   # function to return + 1 step if right and -1 if left
    rnd = 0                         # initialize
    rnd = random.random() * 100     # Using builtin function for random number and convert to percentage
    if rnd > RH:                    # Compare random percentage with User input RH to decide +  or -1 step
        x = -1
    else:
        x = +1
    return x                        # returns +1 if right and -1 if left


def one_walk_steps(ST, MN, MX, RH):     # function to return steps after each walk if min/max/5000 steps is reached
    location = ST                       # initialize initial Start location -user input
    i = 0
    result = 0
    while MX > location > MN and i < 5001:  # iteration until MX / MN or 5000 steps is reached
        x = one_step(RH)                    # calls function one_step to return +1 for right and -1 for left step
        location += x                       # updates to new location
        if location == MX:                  # gives steps in positive value if location MX is reached
            result = i * 1
        elif location == MN:                # gives steps in negative value if location MN is reached
            result = i * -1
        elif i == 5000:                     # returns steps as 5000 if 5000 steps is reached
            result = 5000

        i += 1
    return result


def mul_walk(WK):                           # function for multiple walks (WK - user input of no of walks)
    j = 0                                   #initialize
    hit_all = 0
    hit_min = 0
    hit_max = 0
    hit_5000 = 0
    mean_ows_all = 0
    var_ows_all = 0
    sdv_ows_all = 0
    mean_ows_min = 0
    var_ows_min = 0
    sdv_ows_min = 0
    mean_ows_max = 0
    var_ows_max = 0
    sdv_ows_max = 0
    mean_ows_5000 = 0
    var_ows_5000 = 0
    sdv_ows_5000 = 0

    while j < WK:                                           # iterate until max no of walks user input (WK)
        ows = one_walk_steps(ST, MN, MX, RH)
        hit_all += 1                                        # increment when MN/MX/5000 is reached
        delta_all = abs(ows) - mean_ows_all                 # Citation - Algorithm by Welford for variance/mean for all
        mean_ows_all += delta_all/hit_all
        var_ows_all += delta_all*(abs(ows) - mean_ows_all)
        if hit_all > 1:
            sdv_ows_all = ((var_ows_all / (hit_all - 1)) ** 0.5)
        elif hit_all <= 1:
            sdv_ows_all = None

        if ows < 0:                                         # using above algorithm for the walks to MIN
            hit_min += 1
            delta_min = abs(ows) - mean_ows_min
            mean_ows_min += delta_min/hit_min
            var_ows_min += delta_min*(abs(ows) - mean_ows_min)
            if hit_min > 1:
                sdv_ows_min = ((var_ows_min / (hit_min - 1)) ** 0.5)
            elif hit_min <= 1:
                sdv_ows_min = None
            j += 1

        elif ows == 5000:                                   # using above algorithm for walks with 5000 steps
            hit_5000 += 1
            delta_5000 = abs(ows) - mean_ows_5000
            mean_ows_5000 += delta_5000/hit_5000
            var_ows_5000 += delta_5000*(abs(ows) - mean_ows_5000)
            if hit_5000 > 1:
                sdv_ows_5000 = ((var_ows_5000 / (hit_5000 - 1)) ** 0.5)
            elif hit_5000 <= 1:
                sdv_ows_5000 = None
            j += 1

        elif ows > 0:                                       # using above algorithm for walks to MAX
            hit_max += 1
            delta_max = abs(ows) - mean_ows_max
            mean_ows_max += delta_max/hit_max
            var_ows_max += delta_max*(abs(ows) - mean_ows_max)
            if hit_max > 1:
                sdv_ows_max = ((var_ows_max / (hit_max - 1)) ** 0.5)
            elif hit_max <= 1:
                sdv_ows_max = None
            j += 1

    print("Number of walks that ended on the left:", )
    print("     Number of walks: ", hit_min)
    if hit_min > 0:
        print("     Mean number of steps per walk: ", mean_ows_min)
    elif hit_min == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_min > 1:
        print("     Standard deviation of number of steps per walk: ", sdv_ows_min)
    elif hit_min <= 1:
        print("     Standard deviation of number of steps per walk: N/A")

    print("Number of walks that ended on the right:")
    print("     Number of walks: ", hit_max)
    if hit_max > 0:
        print("     Mean number of steps per walk: ", mean_ows_max)
    elif hit_max == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_max > 1:
        print("     Standard deviation of number of steps per walk: ", sdv_ows_max)
    elif hit_max <= 1:
        print("     Standard deviation of number of steps per walk: N/A")

    print("Number of walks that hit 5000 steps:")
    print("     Number of walks: ", hit_5000)
    if hit_5000 > 0:
        print("     Mean number of steps per walk: ", mean_ows_5000)
    elif hit_5000 == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_5000 > 1:
        print("     Standard deviation of number of steps per walk: ", sdv_ows_5000)
    elif hit_5000 <= 1:
        print("     Standard deviation of number of steps per walk: N/A")

    print("All Walks:")
    print("     Number of walks: ", hit_all)
    if hit_all > 0:
        print("     Mean number of steps per walk: ", mean_ows_all)
    elif hit_all == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_all > 1:
        print("     Standard deviation of number of steps per walk: ", sdv_ows_all)
    elif hit_all <= 1:
        print("     Standard deviation of number of steps per walk: N/A")


mul_walk(WK)
