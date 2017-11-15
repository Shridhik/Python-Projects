

def strt():
    start = input("What is your start location? (between 1 and 499) ")
    if 0 < int(start) < 500:
        return int(start)
    else:
        strt()


def mini(start):
    mn = input("What is your minimum value? (between 0 and " + str(int(start) - 1) + ") ")
    if 0 < int(mn) < int(start) -1:
        return int(mn)
    else:
        mini(start)


def maxi(start):
    mx = input("What is your maximum value? (between " + str(int(start) + 1) + " and 500) ")
    if int(start) + 1 < int(mx) < 500:
        return int(mx)
    else:
        maxi(start)


def rhtprcnt():
    right_percentage = 0
    while int(right_percentage) < 1 or int(right_percentage) > 99:
        right_percentage = input("What is the percentage chance of moving right? (between 1 and 99) ")
        #print(right_percentage)
    return right_percentage


def wlks():
    n_walks = -1
    while int(n_walks) < 0 or int(n_walks) > 10000:
        n_walks = input("How many walks? (between 0 and 10000) ")
        #print(n_walks)
    return n_walks
ST = strt()
MN = mini(ST)
MX = maxi(ST)
RH = rhtprcnt()
WK = wlks()

print("Start   = " , ST)
print("Min     = " , MN)
print("Max     = " , MX)
print("Percent = " , RH)
print("Walks   = " , WK)


