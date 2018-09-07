#Calculates first n triangular numbers by brute force.
def ST1(n):
    y = 1
    i = 0                             #Index to count up to n.
    while i < n:
        x = (1+8*y*y)**0.5            #y is even, replaced y with y = 2y'
        if x.is_integer() == True:
            N = int(y**2)
            print(N)
            i = i + 1
        y = y + 1

#Calculates first n triangular numbers by recusion.
def ST2(n):
    x_n = 1
    y_n = 0
    for i in range(1,n+1):
        m = x_n                     #Saves x_n before reassignment.
        x_n = 3*x_n+4*y_n
        y_n = 2*m+3*y_n
        N = int((y_n/2)**2)
        print(N)

#Calculates first n triangular numbers with Euler's explicit formula.
def ST3(n):
    for i in range(1,n+1):
        a = 3 + 2*(2**0.5)
        b = 3 - 2*(2**0.5)
        c = 4*(2**0.5)
        N = ((a**i - b**i)/c)**2
        print(int(round(N)))
