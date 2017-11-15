#!/usr/bin/python3
#
# Assignment 1
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu
print("program to find the volume of dirt needed for a dirt track") #this is my heading
l = input("straightaway length: ") #input is what is given by the programmer later as a na instruction code
r = input("turn radius: ")
w = input("track width: ")
d = input("track depth: ")
l = .9144 * float(l) #i got conversion rates of yards to meters from google
r = .9144 * float(r) #i got conversion rates of yards to meters from google
w = .3048 * float(w) #i got conversion rates of feet to meters from google
d = .0254 * float(d) #i got conversion rates of inches to meters from google
pi = 3.14159265
v = d * (2 * (l * w) + ((pi * (r + w) ** 2) - ( (pi) * (r) ** 2))) #i did the equation myself on a separate piece of paper
print("volume of dirt needed for a dirt track is: ", v) #summarizing what we just calculated with the program

