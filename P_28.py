import numpy as np

total = [1]
for ii in range(3, 1001+1, 2):
    total.append(ii**2)
    total.append(ii**2-(ii-1))
    total.append(ii**2-2*(ii-1))
    total.append(ii**2-3*(ii-1))

print(np.sum(total))
