def get_a_percentage():
    percentage = 0
    while percentage <1 or percentage > 99:
        try:
            percentage = int (input("What is the percentage"))
            if percentage <1 or percentage > 99:
                print ("Percentage must be between 1 and 99 inclusive, not {0}!".format(percentage))
        except:
            print("you didnt enter a number!")
            percentage = 0
    return percentage
print("you entered {0}".format(get_a_percentage()))



def unit_test ():
        '''
        This is the code that does unit testing!
        '''
        print ("I'm going to run a unit test...")
        print ("You entered {0}".format(get_a_percentage()))

    print ("Hello. My name is {0}. You killed my father. Prepare to die. format(__name__))")

