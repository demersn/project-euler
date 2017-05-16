# Common functions used to solve Project Euler problems
import numpy as np
# Miller-Rabin Primality test in PYHTON
# from https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
# This versions will give correct answers for n less than 341550071728321
# and then reverting to the probabilistic form of the first solution.


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True  # n  is definitely composite


def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in _known_primes[:_precision_for_huge_n])


_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]


# Prime generating from Sieve of Eratosthene
# https://codereview.stackexchange.com/questions/104446/sieve-of-eratosthenes-in-python-3


def candidate_range(n):
    cur = 5
    incr = 2
    while cur < n+1:
        yield cur
        cur += incr
        incr ^= 6  # or incr = 6-incr, or however


def sieve(end):
    prime_list = [2, 3]
    sieve_list = [True] * (end+1)
    for each_number in candidate_range(end):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number*each_number, end+1, each_number):
                sieve_list[multiple] = False
    return prime_list


# Number of divisors (from prime numbers)

# def num_factors(n):
#     primes = []
#     if is_prime(n) is True:
#         nfact = 2
#     else:
#         primes = sieve(np.floor(n**(1/2)))
#         primes = list(reversed(primes))
#         print(primes)
#         while fact != n:
#             fact = pow(primes[ii], po)

#         nfact = 'primes'
#     return nfact


# print(num_factors(12))
