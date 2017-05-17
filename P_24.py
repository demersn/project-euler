# What is the millionth lexicographic permutation of the digits
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# (lexicographic = ascending numerrically)

import itertools

num = list(range(10))
perm = list(itertools.permutations(num))
print(perm[999999])
