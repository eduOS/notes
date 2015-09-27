def amulAdd(a,b):
    if b == 1:
        return a
    else:
        return a + amulAdd(a, b-1)



