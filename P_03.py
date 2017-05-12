# What is the largest prime factor of the number 600851475143
from sieve_prime import sieve
import numpy as np

og_number = 600851475143
number = int(np.ceil(og_number**(1/2)))
test_number = 13195
factors = []


def is_factor(x, y):
    if x % y == 0:
        return True
    else:
        return False


primes = sieve(number)

for y in range(len(primes), 0, -1):
    if y in primes:
        if is_factor(og_number, y) is True:
            factors.append(y)
            break

print(factors)
