import math
m = 0
while True:
    k = math.sqrt(m*(m+1)/2)
    if k.is_integer() == True:
        print(m, int(k))
    m = m +1
