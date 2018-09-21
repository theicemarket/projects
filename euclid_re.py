def gcd(a,b):
    remainders = []
    while b!=0:
        remainders.insert(0, a//b)
        a, b = b, a%b
    x, y = 1, remainders[1]
    for i in range(2,len(remainders)):
        x, y = -y, -x-remainders[i]*y
    return x, -y



def short_gcd(a,b): return a if b==0 else gcd(b, a%b)

def gcq(a,b):
    if b == 0:
        return a
    else:
        return(gcq(b, a%b))
