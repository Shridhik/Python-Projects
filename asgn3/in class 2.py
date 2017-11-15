#
#


import random

def roll_one (n_sides):
    r = random.random()
    result = int(r * n_sides) + 1
    return result

def roll_dice (n_dice, n_sides):
    already_rolled = 0
    total = 0
    while already_rolled < n_dice:
        die = roll_one (n_sides)
        total = total + die
    return total

i = 0
while i < 20:
    print (roll_one(20))
    i = i + 1

