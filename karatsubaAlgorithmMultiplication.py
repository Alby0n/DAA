from math import ceil, floor
def multiply (x,y):
    if x < 10 and y < 10:
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)

    xH = floor(x / 10**m)
    xL = x % (10**m)

    yH = floor(y / 10**m)
    yL = y % (10**m)

    return (xH*yH*(10**(2*m))) + (((xH*yL) + (xL*yH))*10**m ) + (xL*yL)

print (multiply (123,123))