def brute_force():
  m = 0
  while True:
      k = (m*(m+1)/2)**0.5
      if k.is_integer() == True:
          print(m, int(k))
      m = m +1

def pell():
  x = 3
  y = 2
  while True:
    m = x
    x = x**2+2*y**2
    y = 2*m*y
    print((x-1)//2,y//2, "\n")
