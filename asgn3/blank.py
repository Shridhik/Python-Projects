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


def direction():
    outcome = ["left", "right"]         # the result can go either left or right
    direct = random.choice(outcome)     # I found the function random.choice in the python textbook
    #print(direct)
    return direct                       # returns the value of random direction


def one_step(RH):
    rnd = 0
    #dr = direction()
    rnd = random.random() * 100
    #print("RND = ",rnd)
    if rnd > RH:
    #if dr == "left":
        x = -1
    else:
        x = +1
    print(x)
    return x


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
    hit_all = 0
    hit_min = 0
    hit_max = 0
    hit_5000 = 0
    tot_ows_all = 0
    tot_ows_min = 0
    tot_ows_max = 0
    tot_ows_5000 = 0
    mean_ows_all = 0
    mean_ows_min = 0
    mean_ows_max = 0
    mean_ows_5000 = 0
    devmean_all = 0
    devmean_min = 0
    devmean_5000 = 0
    devmean_max = 0
    while j < WK:
        ows= one_walk_steps(ST,MN,MX,RH)
        print("OWS =", ows)
        hit_all = hit_all + 1
        tot_ows_all = tot_ows_all + abs(ows)
        mean_ows_all = tot_ows_all/hit_all
        print("MEAN_OWS_ALL =" , mean_ows_all)

        if ows < 0:
            hit_min = hit_min + 1
            print("HIT_MIN =" , hit_min)
            tot_ows_min = tot_ows_min + abs(ows)
            mean_ows_min = tot_ows_min/hit_min
            print("MEAN_OWS_MIN =" , mean_ows_min)
            devmean_min = devmean_min + ((abs(ows) - mean_ows_min) ** 2)
            print("DEVMEANMIN = ", devmean_min)
            devmean_all = devmean_all + ((abs(ows) - mean_ows_all) ** 2)
            print("DEVMEANALL = ", devmean_all)
            j=j+1

        elif ows == 5000:
            hit_5000 = hit_5000 + 1
            print("HIT_5000 =" , hit_5000)
            tot_ows_5000 = tot_ows_5000 + abs(ows)
            mean_ows_5000 = tot_ows_5000/hit_5000
            print("MEAN_OWS_5000 =" , mean_ows_5000)
            devmean_5000 = devmean_5000 + ((abs(ows) - mean_ows_5000) ** 2)
            print("DEVMEAN5000 = ", devmean_5000)
            devmean_all = devmean_all + ((abs(ows) - mean_ows_all) ** 2)
            print("DEVMEANALL = ", devmean_all)
            j=j+1

        elif ows > 0:
            hit_max = hit_max + 1
            print("HIT_MAX =" , hit_max)
            tot_ows_max = tot_ows_max + abs(ows)
            mean_ows_max = tot_ows_max/hit_max
            print("MEAN_OWS_MAX =" , mean_ows_max)
            devmean_max = devmean_max + ((abs(ows) - mean_ows_max) ** 2)
            print("DEVMEANMAX = ", devmean_max)
            devmean_all = devmean_all + ((abs(ows) - mean_ows_all) ** 2)
            print("DEVMEANALL = ", devmean_all)
            j=j+1


    print("number of walks that ended on the left:", )
    print("     Number of walks: ", hit_min)
    if hit_min > 0:
        print("     Mean number of steps per walk: ", tot_ows_min/hit_min )
        print("     Mean number of steps per walk: ", mean_ows_min )
    elif hit_min == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_min > 1:
        print("     Standard deviation of number of steps per walk: ", (devmean_min/(hit_min - 1)) ** 0.5)
    elif hit_min <= 1:
        print("     Standard deviation of number of steps per walk: N/A")


    print("Number of walks that ended on the right:" )
    print("     Number of walks: ", hit_max)
    if hit_max >  0:
        print("     Mean number of steps per walk: ", tot_ows_max/hit_max)
        print("     Mean number of steps per walk: ", mean_ows_max )
    elif hit_max == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_max > 1:
        print("     Standard deviation of number of steps per walk: ", (devmean_max/(hit_max - 1)) ** 0.5)
    elif hit_max <= 1:
        print("     Standard deviation of number of steps per walk: N/A")



    print("Number of walks that hit 5000 steps:")
    print("     Number of walks: ", hit_5000)
    if hit_5000 > 0:
        print("     Mean number of steps per walk: ", tot_ows_5000/hit_5000 )
        print("     Mean number of steps per walk: ", mean_ows_5000 )
    elif hit_5000 == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_5000 > 1:
        print("     Standard deviation of number of steps per walk: ", (devmean_5000/(hit_5000 - 1)) ** 0.5)
    elif hit_5000 <= 1:
        print("     Standard deviation of number of steps per walk: N/A")


    print("All Walks:")
    print("     Number of walks: ", hit_all)
    if hit_all > 0:
        print("     Mean number of steps per walk: ", tot_ows_all/hit_all )
        print("     Mean number of steps per walk: ", mean_ows_all )
    elif hit_all == 0:
        print("     Mean number of steps per walk: N/A")
    if hit_all > 1:
        print("     Standard deviation of number of steps per walk: ", (devmean_all/(hit_all - 1)) ** 0.5)
    elif hit_all <= 1:
        print("     Standard deviation of number of steps per walk: N/A")

mul_walk(WK)
