from decimal import *
getcontext().prec = 400


def max_length_repeating(limit):
    maxi = 0
    maxi_temp = 0
    maxi_num_temp = 0
    for num in range(1, limit):
        x = Decimal(num)**(-1)
        a = str(x)
        # print(a[1])
        for ii in range(2, len(a)):
            for jj in range(ii+1, len(a)):  # (len(a)-2)/2):
                rep1 = a[ii:jj]
                # print('--1')
                # print(rep1)
                rep2 = a[jj:jj+len(rep1)]
                # print('--2')
                # print(rep2)
                if rep2 != '' and rep2 == rep1 and len(rep1) == len(rep2):
                    # print(len(rep1))
                    maxi_temp = len(rep1)
                    # print(len(rep1))
                    maxi_num_temp = num
                    rep = rep2
                    # print(num)
                    # break

                if maxi_temp > maxi:
                    maxi = maxi_temp
                    maxi_num = maxi_num_temp
                    repp = rep
                    # print(maxi_num)
    return maxi_num, maxi, repp


ans = max_length_repeating(1000)
print(ans)
print(Decimal(ans[0])**(-1))