# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def sum_of_squares(x):
    sum_=0
    for i in range(1,x+1):
        sum_=sum_+i**2
    return sum_

def square_of_sum(x):
    sum_=0
    for i in range(1,x+1):
        sum_=sum_+i
    return (sum_)**2

def diff_sumof_squareof(x):
    return abs(sum_of_squares(x)-square_of_sum(x))

# print(sum_of_squares(10))
# print(square_of_sum(10))
print(diff_sumof_squareof(100))
