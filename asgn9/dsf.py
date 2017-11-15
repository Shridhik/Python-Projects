
def get_a_percentage ():
    percentage = 0
    while percentage < 1 or percentage > 99:
        try:
            percentage = int (input ("What is the percentage? "))
            if percentage < 1 or percentage > 99:
                print ("Percentage must be between 1 and 99 inclusive, not %d!".format (percentage))
        except:
            print ("You didn't enter a number!")
            percentage = 0
    return percentage

def unit_test ():
    '''
    This is the code that does unit testing!
    '''
    print ("I'm going to run a unit test...")
    print ("You entered {0}".format (get_a_percentage()))

print ("Hello.  My name is {0}.  You killed my father.  Prepare to die.".format(__name__))

if __name__ == '__main__':
    unit_test()
