def PT1(N):
    for a in range(1,N+1):
        for b in range(a,N):
            for c in range(b,N):
                if a*a + b*b == c*c:
                    print(a,b,c)

def PT2(N):
    c = 1
    for a in range(1,N+1):
        for b in range(a,N):
            while a*a +b*b <= c:
                if a*a + b*b == c*c:
                    print(a,b,c)
                c = c + 1
