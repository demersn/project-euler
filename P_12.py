# What is the value of the first triangle number
# to have over five hundred divisors?

import numpy as np
from common import sieve


def gen_triangle(x):
    tri = 0
    for i in range(1, x+1):
        tri = tri+i
    return tri


p = list(sieve(70000))


def factors(n, primes):
    if n in primes:
        n_factors = 2
        primes = []
        e = []
    else:
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
            print('oops!')
            print(d)
            print(e)

        n_occurence = []
        for c in range(len(primes)):
            n_occurence.append(e.count(primes[c]))

        n_factors = np.prod(np.array(n_occurence)+1)

    return n_factors, primes, e


def first_to_n_div(n):
    tri = 1
    x = 1
    while factors(tri, p)[0] < n:
        tri = gen_triangle(x)
        x += 1
        # print(gen_triangle(x))
        # print(list_factors(gen_triangle(x)))
        # print(len(factors))
    return gen_triangle(x-1)


print(first_to_n_div(500))
