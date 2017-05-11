# Problem 146
# The smallest positive integer n for which the numbers
# n2+1, n2+3, n2+7, n2+9, n2+13, and n2+27 are consecutive primes is 10.
# The sum of all such integers n below one-million is 1242490.
# What is the sum of all such integers n below 150 million?

from rm_primes import is_prime

# below = 11
below = 1000000
# below = 150000000
sum_int = 0

for n in range(0, below, 2):
    # print(n)
    n1 = n**2+1
    if is_prime(n1) is True:
        n2 = n**2+3
        if is_prime(n2) is True:
            n3 = n**2+7
            if is_prime(n3) is True:
                n4 = n**2+9
                if is_prime(n4) is True:
                    n5 = n**2+13
                    if is_prime(n5) is True:
                        n6 = n**2+27
                        if is_prime(n6) is True:
                            sum_prime = 0
                            for ii in range(n1, n6+1):
                                if is_prime(ii) is True:
                                    sum_prime += 1
                            if sum_prime == 6:
                                sum_int += n

print(sum_int)
# 15.44s
# a = []
# for n in range(1, (11+1)):
#     a.append(n)
# print(a)
