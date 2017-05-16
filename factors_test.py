import numpy as np
from common import sieve


def multi(b):
    out = 1
    for i in range(len(b)):
        out = out*b[i]
    return out


n = 451000
p = list(reversed(sieve(int(n/2))))
# print(p)


primes = []
for ii in range(len(p)):
    if n % p[ii] == 0:
        primes.append(p[ii])


amax = int(np.ceil(np.log(n) / np.log(primes[0])))
print(amax)

e = np.zeros(len(primes))
e[0] = amax
print(e)

for test in range(10):
    l = 0
    m = multi(primes**e)
    print('---')
    print(test)
    print(m)
    print(e)
    if m < n:
        for b in range(l+1, len(primes)):
            e[b] += 1
            m = multi(primes**e)
            print('lower')
            print(e)
            if m > n:
                break
    if m > n:
        if e[l] == 0:
            l += 1
        else:
            e[l] -= 1
        print('greater')
        print(e)
    if m == n:
        break
    print(l)
    # print(m)
    # print(e)
print(e)


a = np.array([1, 1, 2, 2])
print(len(a))
print(np.power(primes, 2))
print(multi(primes**a))
