def gcd(a,b):
        while b!=0:
            c = b
            b = a%b
            a = c
        return(a)

def three(N):
    list = []
    while N not in list:
        list.append(N)
        if N%2 == 0:
            N = N//2
        else:
            N = 3*N +1
    print("L(n)=", len(list), "\nT(n)=", list[-1], "\n", list)

def steps(a,b,m):
    for i in range(m):
        if a%2 == 0 and b%2 == 0:
            a = a//2
            b = b//2
        else:
            a = 3*a
            b = 3*b+1
        print(a,"*k +",b)

def step(a,b,m):
    for i in range(m):
        if (a+b)%2 == 0:
            a = a//2
            b = b//2
        else:
            a = 3*a
            b = 3*b+1
        print(a,"*k +",b)

for i in range(0,100):
    print(i)
