#!/usr/bin/python3
#
# Assignment 2
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu
min = 1 #initializing min value
max = input("what is your maximum number? ") #asking for user input for the max number
#defined function for the guessing game
def guess(min, max):
    mid = (int(max) + int(min))//2 #equation used to cut the number down by 2, eventually narrowing down to the correct number
    print("Is your number (G)reater, (L)ess, or (E)qual to", mid)
    answer = input() #expect the response of G, L, or E
#responses toward the guess either ending the program, or creating a loop
    if answer == "E":
        print("I guessed your number! It was", (mid))
        return
    elif answer == "G":
        guess(mid,max)
    elif answer == "L":
        guess(min,mid)

guess(min,max) #runs the program








