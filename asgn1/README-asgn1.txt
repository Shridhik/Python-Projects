All files for Assignment 1 must go in this directory.
#!/usr/bin/python3
#
# Assignment 1
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu
print("program to find the volume of dirt needed for a dirt track") #this is my heading
l = input("straightaway length: ") #inpu
r = input("turn radius: ")
w = input("track width: ")
d = input("track depth: ")
l = .9144 * float(l) #i got conversion rates of yards to meters from google
r = .9144 * float(r)
w = .3048 * float(w) #i got conversion rates of feet to meters from google
d = .0254 * float(d) #i got conversion rates of inches to meters from google
v = d * (2 * (l * w) + ((3.14159265 * (r + w) ** 2) - ( (3.14159265) * (r) ** 2))) #i did the equation myself on a separate piece of paper
print("volume of dirt needed for a dirt track is: ") #summarizing what we jsut calculated with the program
print(v)
