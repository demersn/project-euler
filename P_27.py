from common import sieve
# from common import is_prime


def n_cons_primes(limit, sieve_limit):
    primes = sieve(sieve_limit)
    n_max = 0
    ab = 0
    bb = 0
    for a in range(-limit, 1, limit):
        for b in range(-limit, 1, limit):
            n = 0
            break_ = 0
            value = (n**2)+(a*n)+b
            while break_ == 0:
                if value in primes:
                    n += 1
                else:
                    break_ = 1
                    n_temp = n
            if n_temp > n_max:
                n_max = n
                ab = a
                bb = b
    return n_max-1, a, b


print(n_cons_primes(50, 1000))
# Doit iterer sur n aussi, a retravailler
