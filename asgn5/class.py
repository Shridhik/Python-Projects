def numbers_only (L):
    new_L= []
    for e in L:
        if isinstance(e, int): #tells
            new_L.append(e)
    return new_L


x = [1, "a", "c", "d", 4, 5, 6, 7.5, 8, 9]
print (numbers_only(x))

