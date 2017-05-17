# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

import numpy as np


def unit(u):  # u from 1 to nine inclusive
    u = int(u)
    if u in [1, 2, 6]:
        l = 3
    elif u in [3, 7, 8]:
        l = 5
    elif u in [4, 5, 9]:
        l = 4
    else:
        l = 0
    return l


def teen(u):  # u from 10 to 19 inclusive
    u = int(u)
    if u == 10:
        l = 3
    elif u in [11, 12]:
        l = 6
    elif u in [13, 14, 18, 19]:
        l = 8
    elif u in [17]:
        l = 9
    elif u in [15, 16]:
        l = 7
    return l


def tens(u):  # 20, 30, etc. to 90:
    uu = int(u[0])
    if uu in [2, 3, 8, 9]:
        l = 6
    elif uu in [4, 5, 6]:
        l = 5
    elif uu == 7:
        l = 7
    return l


a = []
for i in range(1000):
    num = str(i)
    # print(num)
    if len(num) == 1:
        a.append(unit(num))
    elif len(num) == 2:
        if int(num) < 20:
            a.append(teen(num))
        else:
            a.append(tens(num)+unit(num[-1]))
    elif len(num) == 3:
        if int(num[1:]) == 0:
            a.append(unit(num[0])+7)
        elif int(num[1]) == 0:
            a.append(unit(num[0])+7+3+unit(num[-1]))
        elif int(num[1:]) < 20:
            a.append((unit(num[0])+7+3+teen(num[1:])))
        else:
            a.append((unit(num[0])+7+3+tens(num[1:])+unit(num[-1])))

print(np.sum(a))
# One Thousand = 11
print(np.sum(a)+11)
