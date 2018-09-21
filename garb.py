i = 0
while i < 10:
	print(i)
	i = i+1


def PT5(N):
    for a in range(1,N+1):
        for b in range(a,N+1):
            for c in range(b,int((a*a+b*b)**(1/2))+1):
                if a*a + b*b == c*c:
                    print(a,b,c)

def PT5(N):
    bound =  int(N**(1/2))
    for x in range(0,bound):
        t = 2*x+1
        for y in range(x+1,bound):
            s = 2*y+1
            if math.gcd(s,t) == 1:
                for m in range(1,bound):
                    a = m*(s*t)
                    b = m*((s*s - t*t)//2)
                    c = m*((s*s + t*t)//2)
                    if c <= N:
                        print(a,b,c)
