import numpy as np
from common import sieve


def multi(b):
    out = 1
    for i in range(len(b)):
        out = out*b[i]
    return out


# n_factors, primes, e = factors(n)
def factors(n):
    p = list(sieve(int(n/2)))

    primes = []
    for ii in range(len(p)):
        if n % p[ii] == 0:
            primes.append(p[ii])

    d = n
    e = []
    for a in range(len(primes)):
        while d % primes[a] == 0:
            d = d/primes[a]
            e.append(primes[a])

    if np.prod(e) != n:
        print('oops!, n may be prime')

    n_occurence = []
    for c in range(len(primes)):
        n_occurence.append(e.count(primes[c]))

    n_factors = np.prod(np.array(n_occurence)+1)

    return n_factors, primes, e
