def ST1(n):
  y = 0
  i = 0
  while i < n+1:
      x = (1+2*y*y)**0.5
      if x.is_integer() == True:
          N = int((y/2)**2)
          if y != 0:
            print(N)
          i = i + 1
      y = y + 1

def ST2(n):
    x_n = 1
    y_n = 0
    for i in range(1,n+1):
        m = x_n
        x_n = 3*x_n+4*y_n
        y_n = 2*m+3*y_n
        N = int((y_n/2)**2)
        if y_n != 0:
            print(N)

def ST3(n):
    for i in range(1,n+1):
        a = 3 + 2*(2**0.5)
        b = 3 - 2*(2**0.5)
        c = 4*(2**0.5)
        N = ((a**i - b**i)/c)**2
        print(int(round(N)))
