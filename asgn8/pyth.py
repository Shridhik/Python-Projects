#!/usr/bin/python3
# coding=utf-8
#
# Assignment 8
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu

import random               # we will use random.random a lot to create variability


def emptymat(xydim):                            # creates an empty grid
    '''
    Creates an empty grid for initialization
    :param xydim: the dimension of the grid
    :return:
    '''
    matrix = {}                                 # empty dictionary for each pair and value
    for x in range(xydim):                      # goes through every x coordinate up to the input dimension of grid
        for y in range(xydim):                  # goes through every y coordinate pair for every x coordinate to create a square grid
            matrix = {(x, y): '.'}              # returns the value of every coordinate pair as a "." (empty cell)
    return matrix


def day0mat(pop_density, disease_chance, xydim):    # For day 0 of disease, we will need the population density, and the chances of getting a disease
    '''
    Creates a grid for the first day of outbreak
    :param pop_density: This parameter is a number between 0 and 1 which represents the probability that a square starts out occupied. To determine if a cell is occupied at the start
    :param xydim: the dimensions of the grid
    :return:
    '''
    print("Initial Day0 Grid with cells empty - '.' or healthy - '0' or diseased - '1'")
    print("___________________________________________________________________________")
    matrix = {}                                     # created a new dictionary for each coordinate pair and value
    for x in range(xydim):                          # goes through every c coordinate up to the input dimension of grid
        for y in range(xydim):                      # goes through every y coordinate paird for every x coordinate to create a square grid
            prob_occupied = random.random()         # the chance of a cell being occupied by a person is randomly chosen
            prob_diseased = random.random()         # the change of a cell being diseased by a person is randomly generated
            if prob_occupied < pop_density:         # if the probability of an occupied cell is less than the given density
                matrix[(x, y)] = 0                  # then the cell will be a healthy person
                if prob_diseased < disease_chance:  # if the probability of being diseased is less than the chance of getting the disease
                    matrix[(x, y)] = 1              # then the cell will be an unhealthy person
            else:
                matrix[(x, y)] = '.'                # else the cell will be a
            print(matrix[(x, y)], end="")   # print statement that avoids returning line after every print statement, found this soution on https://docs.python.org/3/whatsnew/3.0.html

        print("")                           # print a new line after every line in y has a pair
    print("")
    return matrix

emptymat(2)
day0mat(.5,.5,20)

