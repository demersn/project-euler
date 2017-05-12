#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
def is_natural(x):
    if x%1==0 and x>=0:
        return True
    else:
        return False

def is_pyth_triplet(a,b):
    c2=a**2+b**2
    c=c2**(1/2)
    if is_natural(c)==True:
        #return True
        return int(c)
    else:
        return False

def pyth_triplet_of_sum(x):
    for a in range(1,x+1):
        for b in range(1,x+1):
            c=is_pyth_triplet(a,b)
            if is_natural(is_pyth_triplet(a,b))==True and a+b+c==x and c>0:
                return [a,b,c]

# to find the product abc we use a piece of code from P_8 just for fun
def product_of_string(string):
    prod=1
    for i in range(len(string)):
        prod=prod*int(string[i])
    return prod

def prod_of_pyth_triplet_of_sum(x):
    triplet=pyth_triplet_of_sum(x)
    return product_of_string(triplet)


print(prod_of_pyth_triplet_of_sum(1000))
