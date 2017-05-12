# What is the 10 001st prime number?

def is_prime(y):
    b=int(y**0.5)
    if y % 2 == 0 and y > 2:
        return False
       # check for factors
    for i in range(3,b+1,2):
        if (y % i) == 0:
            return False
    else:
        return True


# print(is_prime(7918))

def n_th_prime(n):
    list_of_prime=[]
    num=2
    while True:
        if len(list_of_prime)==n:
            break
        elif is_prime(num)==True:
            list_of_prime.append(num)
            num=num+1
        else:
            num=num+1
    return list_of_prime[-1]

print(n_th_prime(10001))
