#!/usr/bin/python3
#
# Assignment X
# CMPS 5P, Fall 2016
#
# Sam Student
# sstudent@ucsc.edu
height = input ("How tall is the cone? ")
radius = input ("What is the cone's radius? ")
pi = 3.14159265358979
r = float(radius)
h = float(height)

#calculate the area of the base, which is a circle
base_area = pi * (r**2)

#calculate volume of the cone. Formula by google, quary was "volume of a cone"
v = (1/3) * base_area * h
print("The volume of the cone is:", v)
