# Find the maximum total from top to bottom of the triangle below
# Copy paste from P_18

import numpy as np
triangle = []
with open('p067_triangle.txt') as textFile:
    triangle = [[float(digit) for digit in line.split()] for line in textFile]
# triangle = np.array(triangle)

# triangle = np.array(triangle)
# print(type(triangle[0]))
# for i in range(len(triangle)):
#     m = max(triangle[i])
#     sort_index = np.argsort(triangle[i])
#     sort_index = list(reversed(sort_index[:]))
#     print(sort_index)
#     # me = np.mean(triangle[i])
#     # print(me)
#     # print(triangle[i].index(m))
print(type(triangle))
ii = 0
ind = [ii]
for ll in range(len(triangle)-1):
    if ll < len(triangle)-2:
        p1 = triangle[ll+1][ii]+triangle[ll+2][ii]
        p2 = triangle[ll+1][ii]+triangle[ll+2][ii+1]
        p3 = triangle[ll+1][ii+1]+triangle[ll+2][ii+1]
        p4 = triangle[ll+1][ii+1]+triangle[ll+2][ii+2]
    else:
        p1 = triangle[ll+1][ii]
        p4 = triangle[ll+1][ii+1]
    if max([p1, p2, p3, p4]) in [p1, p2]:
        ii = ii
    elif max([p1, p2, p3, p4]) in [p3, p4]:
        ii = ii+1

    # print(ii)
    ind.append(ii)
# ind.append(9)
print(ind)
a = 0
for p in range(len(triangle)):
    a += triangle[p][ind[p]]
    print(triangle[p][ind[p]])

print(a)
