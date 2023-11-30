def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])
    
def mysum2(L):
    return 0 if not L else L[0] + mysum2(L[1:])

def mysum3(L):
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:])

def mysum4(L):
    first, *rest = L
    return first if not rest else first + mysum4(rest)
    
#print(mysum([1,2,3,4]))

def times(x,y):
    return x * y

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

    
def f1():
    X = 88
    def f2():
        print(X)
    return f2
action = f1()

def maker(N):
    def action(X):
        return X ** N
    return action

def makerLambda(N):
    return lambda X: X ** N

def tester(start):
    state = start
    def nested(lable):
        nonlocal state
        print(lable, state)
        state += 1
    return nested

def f(*args): print(args)

def g(**args): print(args)


def h(a, *pargs, **kargs): print(a, pargs, kargs)

def i(a,b,c,d): print(a,b,c,d)

def l(**args): print(args)

def tracer(func, *pargs, **kargs):
    print('calling', func.__name__)
    return func(*pargs, **kargs)

def func(a,b,c,d) : return a + b + c + d

def konly(a, *b, c): print(a, b, c)

def konly2(a, *, b, c): print(a, b, c)