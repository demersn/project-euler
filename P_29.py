# P_29

limit = 100
comb = []
for a in range(2, limit+1):
    for b in range(2, limit+1):
        comb.append(a**b)

unique = list(set(comb))
# print(sorted(unique))
print(len(unique))
