#Generates Pythagorean Triples
import time
import math

#generates triples by brute force
def PT1(N):
    T0 = time.process_time()
    for a in range(1,N+1):
        for b in range(1,N+1):
            for c in range(1,N+1):
                if a*a + b*b == c*c:
                    print(a,b,c)
    print(time.process_time()-T0)

#brute force optized with a<b<c
def PT2(N):
    T0 = time.process_time()
    for a in range(1,N+1):
        for b in range(a,N+1):
            for c in range(b,N+1):
                if a*a + b*b == c*c:
                    print(a,b,c)
    print(time.process_time()-T0)

#brute force optimized by replacing for loop
def PT3(N):
    T0 = time.process_time()
    for a in range(1,N+1):
        for b in range(a,N+1):
            c = b
            while a*a+b*b >= c*c:
                if a*a + b*b == c*c:
                    print(a,b,c)
                c = c + 1
    print(time.process_time()-T0)

#brute force optimized by starting at next c value instead of b+1
def PT4(N):
    T0 = time.process_time()
    for a in range(1,N+1):
        c = a
        for b in range(a,N+1):
            while a*a+b*b >= c*c:
                if a*a + b*b == c*c:
                    print(a,b,c)
                c = c + 1
    print(time.process_time()-T0)

#generates all pythagorean triples with formulas
def PT5(N):
    T0 = time.process_time()
    bound = int(N**(1/2))
    for x in range(0,bound):
        t = 2*x+1
        for y in range(x+1,bound):
            s = 2*y+1
            if math.gcd(s,t) == 1:
                m = 1
                while m <= bound:           #generates primitive roots then scales
                    a = m*(s*t)
                    b = m*((s*s - t*t)//2)
                    c = m*((s*s + t*t)//2)
                    if c <= N:
                        print(a,b,c)
                    if c > N:
                        m = bound
                    m = m + 1
    print(time.process_time()-T0)
