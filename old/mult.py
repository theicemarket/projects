import math
m = math.pi

for i in range(1,10000000000000):
    k = i*m
    if 1 / (k%1) > i:
        print(i,k-k%1)
