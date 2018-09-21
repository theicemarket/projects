def gcd(a,b):
    r = 1
    while r != 0:
        c = r
        r = a%b
        a = b
        b = r
    print(c)

def garb(n):
    while n < 20:
        if n%2 == 0:
            n = n//2
        else:
            n = 3*n+1
