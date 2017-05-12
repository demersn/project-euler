# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible(x,y):
    if x%y==0:
        return True
    else:
        return False

def make_matrix(count,y):
    list_of_modulus=[]
    for div in range(2,y+1):
        list_of_modulus.append(is_divisible(count,div))
    return list_of_modulus

def smallest_positive_divisible_from(x):  # from 1 to x
    count=1
    while True:
        if all(make_matrix(count,x))==True:
            break
        else:
            count=count+1
            #print(count)
    return count


print(smallest_positive_divisible_from(20))

# This algorithm took 1604.675 seconds to run, about 27 minutes. It needs MAJOR rework, such as eliminating various divisor in the 1 to x range such as 2 4 and 8 for example, because if it's divisible by 8 it will be by 4 and 2 for example.
