# Evaluate the sum of all the amicable numbers under 10000.
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# and each of a and b are called amicable numbers.


def d(n):
    sum_ = 0
    for i in range(1, n):
        if n % i == 0:
            sum_ = sum_+i
            # print(i)
    return sum_


# print(d(220))


def is_amicable(a, b):
    if a == b:
        return False
    elif d(a) == b and d(b) == a:
        return True
    else:
        return False


print(is_amicable(220, 284))


# From P_16
# def sum_of_string(string):
#     sum_ = 0
#     for i in range(len(string)):
#         sum_ = sum_+int(string[i])
#     return sum_


def sum_of_amicable_under(x):
    sum_amicable = 0
    for a in range(x+1):
        for b in range(x+1):
            if is_amicable(a, b) is True and a != b:
                sum_amicable += a+b
    return sum_amicable


print(sum_of_amicable_under(500))
