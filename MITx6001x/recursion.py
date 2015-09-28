def amulAdd(a,b):
    if b == 1:
        return a
    return a + amulAdd(a, b-1)

def classive(a):
    if a == 1:
        return 1
    return a*classive(a-1)

def powerNew(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        return powerNew(base*base, exp/2)
    return base*powerNew(base,exp-1)

def gcdIter(a,b):
    m = min(a,b)
    while a%m != 0 or b%m != 0:
        m -= 1
    return m

def gcdRecur(a,b):
    if b == 0:
        return a
    return gcdRecur(b, a%b)

#def hanoi(n, fr, to, sp):
def printMove(fr, to):
    print 'move from ' + fr + ' to ' + to

def tower(n, fr, to, sp):
    if n == 1:
        printMove(fr,to)
    else:
        tower(n-1, fr, sp, to)
        tower(1, fr, to, sp)
        tower(n-1, sp, to, fr)


