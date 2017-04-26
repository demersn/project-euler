
def is_prime(y):
    #b=int(y**0.5)
    if y % 2 == 0 and y > 2:
        return False
       # check for factors
    for i in range(3,2,y):
        if (y % i) == 0:
            return False
    if y<2:
        return False
    else:
        return True

def n_cons_primes(range_):
    for a in range(-range_,1,range_):
        for b in range(-range_,1,range_):
            n=0
            break_=0
            value=n^2+a*n+b
            while break_==0:
                if is_prime(value)==True:
                    n=n+1
                else:
                    break_=1
                    return n-1

print(n_cons_primes(50))
# Doit iterer sur n aussi, a retravailler
