
nfile_o = open(input('Which file would you like to import? '))
nfile_o = nfile_o.read()
nfile_o = nfile_o.lower()
nfile_o = nfile_o.strip().split()
nfile = []          #Initialization, his must be on the outside of the for loop otherwise only the last term will be appended
for i in nfile_o:       #This is the for loop that removes any non-alphabetical or numerical items
    if i.isalpha() or i.isalnum():
        nfile.append(i)
# print(nfile)

# print(nfile.sort())       #This is to check to see if the sort works before the function runs to check if errors are in the function or the list cleaning


def sort(nfile):
    A = nfile[:]
    B = []
    A.append(False)
    B.append(False)
    # print(A)
    # print(B)
    previous = 'z' * 100
    last_append = 'a'
    while True:
        if A[0] != False and B[0] == False:     #this is for when B is false but A isn't false
            if A[0] < previous:                 #this if statement is for when A[i] is less than the previously appended value so it should be appended on the other list
                previous = A[0]                 #sets the previous value equal to the current value of A[i] for the next run through
                if last_append == 'b':
                    last_append = 'a'           #sets the last list to be append to 'a'...
                    A.append(A[0])              #...and then appends A[i] to list A
                    del A[0]
                elif last_append == 'a':
                    last_append = 'b'
                    B.append(A[0])
                    del A[0]
            elif A[0] >= previous:                #this is for when A[i] is greater than the previous value so it should be appended behind the previous value
                previous = A[0]
                if last_append == 'a':
                    A.append(A[0])
                    del A[0]
                elif last_append == 'b':
                    last_append = 'a'
                    A.append(A[0])
                    del A[0]
        elif A[0] == False and B[0] != False:     #this is for when A is false but B isn't false
            if B[0] < previous:
                previous = B[0]
                if last_append == 'b':
                    last_append = 'a'
                    A.append(B[0])
                    del B[0]
                elif last_append == 'a':
                    last_append = 'b'
                    B.append(B[0])
                    del B[0]
            elif B[0] >= previous:
                previous = B[0]
                if last_append == 'a':
                    A.append(B[0])
                    del B[0]
                elif last_append == 'b':
                    B.append(B[0])
                    del B[0]
        elif A[0] != False and B[0] != False:     #this is for when neither A nor B are false
            if A[0] >= previous and B[0] >= previous:
                if A[0] >= B[0]:
                    previous = B[0]
                    if last_append == 'a':
                        A.append(B[0])
                        del B[0]
                    elif last_append == 'b':
                        B.append(B[0])
                        del B[0]
                elif A[0] < B[0]:
                    previous = A[0]
                    if last_append == 'a':
                        A.append(A[0])
                        del A[0]
                    elif last_append == 'b':
                        B.append(A[0])
                        del A[0]
            elif A[0] >= previous > B[0]:
                previous = A[0]
                if last_append == 'a':
                    A.append(A[0])
                    del A[0]
                elif last_append == 'b':
                    B.append(B[0])
                    del B[0]
            elif A[0] < previous <= B[0]:
                previous = B[0]
                if last_append == 'a':
                    A.append(B[0])
                    del B[0]
                elif last_append == 'b':
                    B.append(B[0])
                    del B[0]
            elif A[0] < previous and B[0] < previous:
                if A[0] >= B[0]:
                    previous = B[0]
                    if last_append == 'a':
                        last_append = 'b'
                        B.append(B[0])
                        del B[0]
                    elif last_append == 'b':
                        last_append = 'a'
                        A.append(B[0])
                        del B[0]
                elif A[0] < B[0]:
                    previous = A[0]
                    if last_append == 'a':
                        last_append == 'b'
                        B.append(A[0])
                        del A[0]
                    elif last_append == 'b':
                        last_append = 'a'
                        A.append(A[0])
                        del A[0]
        elif A[0] == False and B[0] == False and len(A) == 1:
            del A[0]
            del B[0]
            print(A)
            print(B)
            return B
        elif A[0] == False and B[0] == False and len(B) == 1:
            del A[0]
            del B[0]
            return A
        elif A[0] == False and B[0] == False and len(A) > 1 and len(B) > 1:
            A.append(False)
            B.append(False)
            del A[0]
            del B[0]
            previous = 'z' * 100

sorted_list = sort(nfile)


def histogram(sorted_list):
    counted_list = []
    frequency = []
    for i in sorted_list:
        if i not in counted_list:
            counted_list.append(i)
            frequency.append(1)
        else:
            loc = counted_list.index(i)
            frequency[loc] += 1
    for i in range(len(counted_list)):
        print(frequency[i], counted_list[i])

histogram(sorted_list)

