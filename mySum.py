def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])

def mysum4(L):
    first, *rest = L
    return first if len(L) == 1 else L[0] + mysum3(rest)
    
#print(mysum([1,2,3,4]))

def times(x,y):
    return x * y

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

    