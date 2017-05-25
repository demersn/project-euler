# P_15
# Takes way too long to compute for size = 20, needs more thinking
import numpy as np

size = 4
size += 1
g = list(reversed(range(1, size+1)))


def sublist(input):
    sub = []
    for tt in range(len(input)):
        a = input[tt:]
        sub.append(a)
    return sub


gg = sublist(g)
print(gg)

for ii in range(size-3):
    g = sublist(g)

# print(g)
for l in range(len(g)):
    g = np.sum(g)
print(g)

