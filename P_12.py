# What is the value of the first triangle number 
# to have over five hundred divisors?


def gen_triangle(x):
    tri = 0
    for i in range(1, x+1):
        tri = tri+i
    return tri


print(gen_triangle(3))


def is_factor(x, y):
    if x % y == 0:
        return True
    else:
        return False


def num_factors(x):
    factors = 0
    for i in range(1, x+1):
        if is_factor(x, i) is True:
            factors += 1
    return factors

# print(list_factors(28))


def first_to_n_div(n):
    tri = 1
    x = 1
    while num_factors(tri) < n:
        tri = gen_triangle(x)
        x += 1
        # print(gen_triangle(x))
        # print(list_factors(gen_triangle(x)))
        # print(len(factors))
    return gen_triangle(x-1)


print(first_to_n_div(500))
