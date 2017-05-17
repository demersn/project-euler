from decimal import *
getcontext().prec = 100


def max_length_repeating(limit):
    maxi = 0
    maxi_temp = 0
    maxi_num_temp = 0
    for num in range(1, limit):
        x = Decimal(num)
        a = x**(-1)
        # print(a)
        a = str(a)
        # print(a[1])
        out = 0
        for ii in range(2, len(a)):
            for jj in range(ii+1, len(a)):  # (len(a)-2)/2):
                if out == 0:
                    rep1 = a[ii:jj]
                    # print('--1')
                    # print(rep1)
                    rep2 = a[jj+1:jj+1+len(rep1)]
                    # print('--2')
                    # print(rep2)
                    if rep2 != '' and rep2 in rep1:
                        # print(len(rep1))
                        maxi_temp = len(rep1)
                        # print(len(rep1))
                        maxi_num_temp = num
                        # print(num)
                        out = 1
                        break
                else:
                    break
                # print(out)
        if maxi_temp > maxi:
            maxi = maxi_temp
            maxi_num = maxi_num_temp
            # print(maxi_num)
    return maxi_num, maxi


print(max_length_repeating(1000))
print(Decimal(102)**(-1))