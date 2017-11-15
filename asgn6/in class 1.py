def count_words(L):
    d = dict()              # d is the dictionary into which we'll put the histogram
    for word in L:
        d[word] = d.get (word, 0) + 1
    return (d)

result = count_words ("the quick brown fox runs over the lazy dog".split())
print (result)
for word in sorted(result.keys()):
    print (word, result[word])

