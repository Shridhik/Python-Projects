#!/usr/bin/python3
# coding=utf-8
#
# Assignment 7
# CMPS 5P, Fall 2016
#
# Shridhik John
# shjohn@ucsc.edu


import VideoPoker
import random

vp = VideoPoker.VideoPoker()


def inpcredit():
    credit = 0
    while credit < 10 or credit > 1000:         # parameteters ensuring that the input credits are valid
        credit = int(input("How many credits would you like[10-1000]? "))  # turns the input into an interger for videopoker to process
    return credit


def shufdeck():     # function to shuffle deck           # went to Ocean office hours
                    # should return 5 random cards from a deck
    cardrank = "23456789TJQKA"
    cardsuit = "CDHS"
    deck = []

    for i in cardsuit:  # for loop that makes each type of card
        for e in cardrank:
            deck.append(e+i)            # appends each possibility card to the list, deck, with carduit+cardrank
            random.shuffle(deck)        # randomly shuffles Deck
    return deck                         # after a deck is created, a random first five will be selected for your hand


def rankcount(uhand):
    rankl = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for rank in uhand:              # for every element in uhand, the number will be appended to the list of rankl
        if rank[0] == "2":
            rankl[0] += 1
        elif rank[0] == "3":
            rankl[1] += 1
        elif rank[0] == "4":
            rankl[2] += 1
        elif rank[0] == "5":
            rankl[3] += 1
        elif rank[0] == "6":
            rankl[4] += 1
        elif rank[0] == "7":
            rankl[5] += 1
        elif rank[0] == "8":
            rankl[6] += 1
        elif rank[0] == "9":
            rankl[7] += 1
        elif rank[0] == "T":
            rankl[8] += 1
        elif rank[0] == "J":
            rankl[9] += 1
        elif rank[0] == "Q":
            rankl[10] += 1
        elif rank[0] == "K":
            rankl[11] += 1
        elif rank[0] == "A":
            rankl[12] += 1
    return rankl


def suitcount(userhand):        # This function will count the amount of suits in the user's hand
    suitl = [0, 0, 0, 0]
    for suit in userhand:
        if suit[1] == "C":      # CDHS order
            suitl[0] += 1
        if suit[1] == "D":
            suitl[1] += 1
        if suit[1] == "H":
            suitl[2] += 1
        if suit[1] == "S":
            suitl[3] += 1
    return suitl


def listtostr(inplst):      # function that turns the list of suits and ranks into strings
    nstr = ''
    for e in inplst:
        nstr += ''.join(str(e))         # googled how to turn lists into string, and found this method on http://stackoverflow.com/questions/4481724/convert-a-list-of-characters-into-a-string
    return nstr


def rank_hand(rstr, sstr):              # function that ranks all the types of poker hands, takes rank string and suit string as arguments
    rank = 10                           # initialization of rank of hand (default value)
    isflush = 0                         # initialization of is flush 0
    cons = 0                            # initialization of consecutive numbers
    have1 = 0                           # initialization of have1 (if  the rank has 1)
    srank = 'Your Hand is a Bust! No credits for you!'       # Anything else
    pos = 0                               # else position is 0 and have1 variable set to 0
    pos2 = 0                            # same as above
    for e in sstr:                      # traverses through every element in suit string
        if e == '5':                    # if any element in suit is 5 that means it is a flush
            isflush = 1                 # update isflush to 1 which is used later
            rank = 5                    # according to wikipedia, this ranks as a 5
            srank = "Flush"             # stores string Flush that is returned by the function
            for c in rstr:              # traverses through every element in rank string
                if c == '1':            # if the element (rank) occurs once
                    pos = rstr.index(c)  # the positional index of the first occurance of 1 is recorded

            for i in range(pos, pos+5):  # we will look at the next five elements from that position
                if pos <= 8:
                    if int(rstr[i]) == 1:          # if consequtive are only 1's
                        cons += int(rstr[i])    # adds the value of each consective elements
            if pos == 8 and cons == 5:  # if first "1" is in pos=8 (rank=Ten) and we have consecutive five '1's that is a royal flush
                rank = 1
                srank = "Royal Flush"
            elif pos <= 8 and cons == 5:  # if first "1" is less than pos=8 (any rank less than Ten) and we have consecutive '1's that is a Straight flush
                rank = 2
                srank = "Straight Flush"
            elif pos == 0 and cons == 4 and rstr[12] == '1':  # same as above except one combination which is A[rstr[12]=1],2[pos=0],3,4,5[cons=4]
                rank = 2
                srank = "Straight Flush"

    if isflush == 0:        # if the rank is not a flush
        combc = 0           # initializing of combination of 3 and 2 for Full house
        npair = 0           # initializing no of pairs to 0
        for c in rstr:      # traverse through every eleiment in rank string
            if c == '4':            # if a rank occurs 4 times, it will result in 4 of a kind
                rank = 3
                srank = 'Four of a kind'
            elif c == '3' and c != '2':  # if rank occurs 3 times but does not have a rank occuring 2 times then it is Three of a kind
                rank = 7
                srank = 'Three of a kind'
            elif c != '4' and c != '1' and c != '0':  # if rank has only 3 times or 2 times
                    combc += int(c)                  # adding the ranks of those 2 ranks
                    if combc == 5:                   # if total =5 that means there is only one 3 and one 2 in ranks and it is a Full House
                        rank = 3
                        srank = 'Full House'
                    if c == '2':                     # if rank has 2 (pair)
                        pos = rstr.index(c)          # checking for the position of rank which has value 2 for Jack or Better
                        npair += 1                   # adding no of pairs(ranks that have value'2'
                        if npair == 2:               # if 2 pairs then it is Two Pair
                            rank = 8
                            srank = 'Two Pair'
                        elif npair == 1 and pos >= 9:  # if 1 pair and pos is greater than 9(J) (Jack or Better)
                            rank = 9
                            srank = 'Jacks or Better'

            elif c == '1':                            # if not flush and if rank has value 1
                pos2 = rstr.index(c)                   # get position of that rank
                have1 = 1                             # change have1 variable to 1
        for i in range(pos2, pos2+5):                   # from that position
            if pos2 <= 8:
                if int(rstr[i]) == 1:
                    cons += int(rstr[i])                  # add consecutive 1's
        if have1 == 1 and pos2 <= 8 and cons == 5:     # if have1 is true and position is less than 8(T) and consecutive 1's in next 5 elements in rank string it is a straight
            rank = 6
            srank = "Straight"
        elif have1 == 1 and pos2 == 0 and cons == 4 and rstr[:4] == '1111' and rstr[12] == '1':  # same as above but for A,2,3,4,5 is also straight
            rank = 6
            srank = "Straight"
    # print("ISFLUSH=", isflush)
    # print("POS=", pos)
    # print("POS2=", pos2)
    # print("CONS=", cons)
    # print("RANK=", rank)
    # print("SRANK=", srank)
    return srank                                       # returns the string srank for playloop where it is used in calculating credits


b = ['5C', 'AC', '9H', 'AS', '7S', '5D', 'AD', '9D', '8D', '7D']     # test hand to run and checks program


def playloop(cred, hand):                   # play loop for the video poker (using module VideoPoker.py) with arguments credit and the hand
    ncred = 0                               # initializes no of credits to 0
    vp.display_credits(cred)                # displays the credit based on user input
    vp.set_status("Please make a bet!")     # Displays status to request user to Place a bet
    bet = vp.get_credits_bet()              # Stores the value of the bet
    vp.set_status(str(bet))                 # displays the value of bet
    if cred >= bet:                         # if the amount of credits you have are greater than whatever you can bet:
        cred = cred - bet                   # reduces the available credit based on bet
    elif cred < bet:                        # if you have less credits than you can bet:
        vp.set_status("Sorry, You have less credits than you can bet!!")
        hand = shufdeck()
        vp.await_continue_button()
        playloop(cred, hand)
    elif cred == 0:
        vp.set_status("Sorry, You are out of credits!!")
        vp.await_continue_button()
    vp.display_credits(cred)                # displays the current credit (inital - bet)
    vp.set_cards(hand[:5])                      # displays the hand when credit is selected
    lheld = vp.get_held_cards()                 # gets the list of the held cards
    lenlheld = len(lheld)                   # length of the list of held cards
    strlheld = listtostr(lheld)             # converts it into a string
    e = strlheld                            # stores the string of the held list in variable e
    if lenlheld < 5:                        # Will detect if something is held
        if lenlheld == 0:                   # if nothing is held, all of the cards will change
            hand[0] = hand[5]
            hand[1] = hand[6]
            hand[2] = hand[7]
            hand[3] = hand[8]
            hand[4] = hand[9]
        # When the first card is not held,(e != 0)
        if e == '1234' or e == '123' or e == '234' or e == '134' or e == '124' or e == '12' or e == '13' or e == '14' or e == '23' or e == '24' or e == '34' or e == '1' or e == '2' or e == '3' or e == '4':
            hand[0] = hand[5]
        # When the second card is not held,(e != 1)
        if e == '0234' or e == '023' or e == '234' or e == '034' or e == '024' or e == '02' or e == '03' or e == '04' or e == '23' or e == '24' or e == '34' or e == '0' or e == '2' or e == '3' or e == '4':
            hand[1] = hand[6]
        # When the third card is not held,(e != 2)
        if e == '0134' or e == '013' or e == '134' or e == '034' or e == '014' or e == '01' or e == '03' or e == '04' or e == '13' or e == '14' or e == '34' or e == '0' or e == '1' or e == '3' or e == '4':
            hand[2] = hand[7]
        # When the fourth card is not held,(e != 3)
        if e == '0124' or e == '012' or e == '124' or e == '024' or e == '014' or e == '01' or e == '02' or e == '04' or e == '12' or e == '14' or e == '24' or e == '0' or e == '1' or e == '2' or e == '4':
            hand[3] = hand[8]
        # When the fifth card is not held,(e != 4)
        if e == '0123' or e == '012' or e == '123' or e == '023' or e == '013' or e == '01' or e == '02' or e == '03' or e == '12' or e == '13' or e == '23' or e == '0' or e == '1' or e == '2' or e == '3':
            hand[4] = hand[9]

        print(hand[:5])                             # prints the hand in console
        vp.set_cards(hand[:5])
    rst = listtostr(rankcount(hand[:5]))        # converts the list of rank to string
    # print(rst)
    sst = listtostr(suitcount(hand[:5]))        # converts the list of suit to string
    # print(sst)
    srnk = rank_hand(rst, sst)              # returns the string for credit calculations based on the ranking of existing hand
    # print(srnk)
    vp.set_status(srnk)                     # displays on the Graphical interface
    while vp.await_continue_button() == 0:  # if continue button is not pressed
        vp.set_status(srnk)                 # display the strin of Ranking of the existing hand
    else:                                   # if Continue button is pressed
        if srnk == "Royal Flush":           # if Ranking is Royal Flush
            if bet < 5:                     # if bet=5 credit is added by 4000 if not credit is bet * 250
                ncred = bet * 250
            elif bet == 5:
                ncred = 4000
        elif srnk == "Straight Flush":      # if Ranking is Straight Flush
            ncred = bet * 50
        elif srnk == "Four of a kind":      # if Ranking is Four of a kind
            ncred = bet * 25
        elif srnk == "Full House":          # if Ranking is Full House
            ncred = bet * 9
        elif srnk == "Flush":               # if Ranking is Flush
            ncred = bet * 6
        elif srnk == "Straight":            # if Ranking is Straight
            ncred = bet * 4
        elif srnk == "Three of a kind":      # if Ranking is Three of a kind
            ncred = bet * 3
        elif srnk == "Two Pair":             # if Ranking is Two Pair
            ncred = bet * 2
        elif srnk == "Jacks or Better":      # if Ranking is Jacks or Better
            ncred = bet * 1

        cred += ncred                       # adds the existing credit to the gain or loss in the bet
        print(cred)
        hand = shufdeck()
        playloop(cred, hand)                # loops back (Recursion)
    return


playloop(inpcredit(), shufdeck())


# after you shuffle it, you create a ranking function
# make it return a string with 0s and 1s
# create a deck
# create a hand from that deck
# create a play loop
# display the credits
# create mechanism to increase and decrease credits
# ranking system
# held cards
# deal function to deal cards
