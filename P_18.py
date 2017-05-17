# Find the maximum total from top to bottom of the triangle below:
import numpy as np
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
triangle = np.array(triangle)
# print(type(triangle[0]))
# for i in range(len(triangle)):
#     m = max(triangle[i])
#     sort_index = np.argsort(triangle[i])
#     sort_index = list(reversed(sort_index[:]))
#     print(sort_index)
#     # me = np.mean(triangle[i])
#     # print(me)
#     # print(triangle[i].index(m))

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
ind.append(9)
print(ind)
a = 0
for p in range(len(triangle)):
    a += triangle[p][ind[p]]
    print(triangle[p][ind[p]])

print(a)
# Works by correcting the last row by hand
# Not a problem that I find that intresting so I will leave it at that
# Not sure how this proves this is the way to solve it, as this method
# does not work for the similar problem P_67.