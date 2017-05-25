# P_15
import numpy as np
size = 3
# [ii] denotes the horizontal [ - ] line index of the grid


# init = np.zeros(size)
# z = init
# temp = init
# ind = 1
# grid = []
# for ii in range(1, size)
#     for jj in range(size+1):
#         a = z
#         a[ii][-11]

# grid = np.reshape(grid, (len(grid)/2, 2))


# print(grid)
# print(len(grid))

l = list(reversed(range(1, size+1)))
# l = list(reversed(l))
print(l)
s = size+2
for ii in range(len(l)):
    s += np.sum(l[ii:])

print(s)
