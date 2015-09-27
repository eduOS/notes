def findRoot3(x, power, epilon):
    '''
    x and epsilon int or float, power an int
      epilon > 0 & power >= 1
    returns a float y s. t. y**power is within epilon of x
    if such a float does not exist, it returns None
    '''
    if x < 0 and power%2 == 0:
        return None
    # cannot find even powered root of a negative number
    low = min(-1, x)
    high = max(1, x)
    # specifications for abs(x) < 1 and x < -1
    ans = (low + high)/2.0
    while abs(ans**power - x) > epilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2.0
    return ans


