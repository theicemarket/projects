def gcf(a,b):
    r = a % b
    while r > 0: (a, b, r) = (b, r, b%r); print(a)



def gce(a,b):
        while b!=0:
            c = b
            b = a%b
            a = c
        return(a)

def gce(b,a):
        while a!=0: temp = a; a = b%a; b = temp
        return(b)

def gcd(a,b): return a if b==0 else gcd(b, a % b)

def gcq(a,b):
    if b == 0:
        return a
    else:
        return(gcd(b, a%b))
