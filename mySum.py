def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
#print(mysum([1,2,3,4]))

def times(x,y):
    return x * y

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

    