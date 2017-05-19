# P_30
import numpy as np

limit = 7*9**5
p = 5
comb = []
for ii in range(2, limit):
    a = [int(x) for x in str(ii)]
    po = np.power(a, p)
    tsum = np.sum(po)
    if tsum == ii:
        comb.append(ii)

print(comb)
print(np.sum(comb))
