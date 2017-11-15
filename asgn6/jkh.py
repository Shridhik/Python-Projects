


import os.path
comb_hist_words ={}
comb_hist_char ={}
comb_hist_bi ={}
comb_hist_tri ={}
comb_tot_word = 0
comb_tot_char = 0
comb_tot_bi   = 0
comb_tot_tri = 0

comb_list_words =[]
comb_list_char =[]
comb_list_bi =[]
comb_list_tri =[]

def openfile():

    aval = False
    while not aval:
        filename = input("What file do you want to import? ", )
        aval = os.path.isfile(filename)
        if aval:
            return filename
        if len(filename)<1:
            break
        elif if aval:
            print("I don't recognize the file,", filename, "Try Again!!!")

            print("")
allfile()

