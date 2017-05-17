# Evaluate the sum of all the amicable numbers under 10000.
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.

lim = 10001


def d(n):
    sum_ = 0
    for i in range(1, n):
        if n % i == 0:
            sum_ = sum_+i
            # print(i)
    return sum_


amicable_list = []
for ii in range(lim):
    amicable_list.append([ii, d(ii)])

# print(amicable_list)


def is_amicable(a, b):
    if a == b:
        return False
    elif (amicable_list[a][1] == amicable_list[b][0]
            and amicable_list[b][1] == amicable_list[a][0]):
        return True
    else:
        return False


print(is_amicable(284, 220))


def sum_of_amicable_under(x):
    sum_amicable = 0
    for a in range(x):
        for b in range(x):
            if is_amicable(a, b) is True and a != b:
                sum_amicable += a+b
    return (sum_amicable/2)  # The result is doubled as they both go up


print(sum_of_amicable_under(lim))

# There is probably as way to eliminate the need to divide by 2 at the end
# and save on time, but as of right now, I am not sure how.
