import scipy.misc as sp
import numpy as np

limit = int(sp.factorial(9))
curious = []
for ii in range(limit):
    s = str(ii)
    temp_sum = 0
    for jj in range(len(s)):
        # print(s[jj])
        temp_sum += sp.factorial(int(s[jj]))
    if temp_sum == ii:
        curious.append(ii)

print(curious)
curious = curious[2:]  # Remove 1 and 2
print(np.sum(curious))
