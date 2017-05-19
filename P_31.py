# P_31
import numpy as np

coins = [200, 100, 50, 20, 10, 5, 2, 1]
total = 200

# for p1 in range(int(total/coins[0])):
#     for p2 in range(int(total/coins[1])):
#         for p3 in range(int(total/coins[2])):
#             for p4 in range(int(total/coins[3])):
#                 for p5 in range(int(total/coins[4])):
#                     for p6 in range(int(total/coins[5])):
#                         for p7 in range(int(total/coins[6])):
#                             for p8 in range(int(total/coins[7])):
#                                 comb = [p1, p2, p3, p4, p5, p6, p7, p8]
ways = 0
al = []
good = []

for p1 in range(0, total+1, coins[0]):
    for p2 in range(p1, total+1, coins[1]):
        for p3 in range(p2, total, coins[2]):
            for p4 in range(p3, total, coins[3]):
                for p5 in range(p4, total, coins[4]):
                    for p6 in range(p5, total, coins[5]):
                        for p7 in range(p6, total, coins[6]):
                            for p8 in range(p7, total, coins[7]):
                                comb = [p1, p2, p3, p4, p5, p6, p7, p8]
                                al.append(comb)
                                if np.sum(comb) == 200:
                                    ways += 1
                                    good.append(comb)

print(ways)
