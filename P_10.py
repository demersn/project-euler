# Find the sum of all the primes below two million

#from problem 7 and 3 we have is_prime
def is_prime(y):
    b=int(y**0.5)
    if y % 2 == 0 and y > 2:
        return False
       # check for factors
    for i in range(3,b+1,2):
        if (y % i) == 0:
            return False
    if y<2:
        return False
    else:
        return True

# and from problem 8 we have product of string, modded to have
def sum_of_string(string):
    sum_=0
    for i in range(len(string)):
        sum_=sum_+int(string[i])
    return sum_

def sum_of_primes_below(x):
    primes=[]
    for i in range(x):
        if is_prime(i)==True:
            primes.append(i)
    sum_=sum_of_string(primes)
    return sum_

print(sum_of_primes_below(2000000))
