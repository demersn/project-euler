# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(x,y):
    if x%y==0:
        return True
    else:
        return False

def smallest_positive_divisible_from(x):  # from 1 to x
    count=1
    while True:
        for div in range(2,x+1):
            if is_divisible(count,div) == True:
                return count
            else:
                count=count+1
                print(count)
                print(div)
                print(x)


print(smallest_positive_divisible_from(10))
