def get_primes(n):
    numbers = set(range(n, 1, -1))
    k = 0
    while numbers:
        p = numbers.pop()
        k = k + 1/p
        numbers.difference_update(set(range(p*2, n+1, p)))
    return k
