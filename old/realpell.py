x = 1
y = 1

while True:
        m = x
        x = x**2+2*y**2
        y = 2*m*y
        print((x-1)//2,y//2, "\n")
