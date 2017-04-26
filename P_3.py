# What is the largest prime factor of the number 600851475143

def is_factor(x,y):
    if x%y==0:
        return True
    else:
        return False

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

def largest_prime_factor(x):
    for y in range(x-1,0,-1):
        if is_prime(y)==True:
            if is_factor(x,y)==True:
                break
    return y
test_y=13195
test_x=600851475143

#print(is_factor(test_x,test_y))
#print(is_prime(test_y))
#print(largest_prime_factor(test_x))
def list_prime(x):
    for y in range(x-1,0,-1):
        if is_prime(y)==True:
            print(y)
    return y


print(largest_prime_factor(600851475143))
