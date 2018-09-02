import random
import math

x = 10**140
y = 10**200
i = 0
pseu_primes = []
while i != 2:
    a = random.randint(x,y)
    b = 2
        if pow(b,a-1,a) == 1:
        pseu_primes.append(a)
        print(a)
        i = i+1
print(pseu_primes)
