import math

def dec2bin(f):
    if f >= 1:
        g = int(math.log(f, 2))
    else:
        g = -1
    h = g + 1
    ig = math.pow(2, g)
    st = ""    
    while f > 0 or ig >= 1: 
        if f < 1:
            if len(st[h:]) >= 10: # 10 fractional digits max
                   break
        if f >= ig:
            st += "1"
            f -= ig
        else:
            st += "0"
        ig /= 2
    st = st[:h] + " " + st[h:]
    return st


while True:
    f = float (input ("desiatkove cislo: "))
    if f <= 0: break
    print ("binarne ", dec2bin(f))
