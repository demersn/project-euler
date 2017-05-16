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
print(e)
e_next = np.zeros(len(primes))
e_next[0] = amax
print(e-e_next)
i_last = np.nonzero(e-e_next)[0][0]
print(len(primes))

for test in range(10):
    l = 0
    m = multi(primes**e_next)
    print('---')
    print(test)
    print(m)
    print(np.nonzero(e-e_next))
    i_last = np.nonzero(e-e_next)[0][-1]  # last index where e differs from e_next
    i_first = np.nonzero(e-e_next)[0][0]  # first index where e differs
    print(i_last)
    e = np.copy(e_next)  # Make changes to e_next
    if m < n:
        if len(primes)-1 == i_last:
            pass
            # e_next[i_first+1] += 1
            # e_next[l+2::].fill(0)
            # e = np.copy(e_next)
            # e[l+1] += 1
            # # print(e)
            # print(e_next)
        else:
            for b in range(i_last+1, len(primes)):
                e_next[b] += 1
                m = multi(primes**e_next)
                print('lower')
                print(e_next)
                if m >= n:
                    break
    if m > n:
        if e_next[l] == 0:
            l += 1
        else:
            e_next[l] -= 1
        #     if e_next[l+1] == 0:
        #         pass
        #     else:
        #         e_next[l+1] -= 1
        print('greater')
        print(e_next)
        # print(e)
    if m == n:
        break
    print(l)
    # print(m)
    # print(e)
print(e_next)

print('----- end loop')
a = np.array([1, 1, 2, 2])
print(len(a))
print(np.power(primes, 2))
print(multi(primes**a))
