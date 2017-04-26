# Find the sum of the digits in the number 100!

# From P_16
def sum_of_string(string):
    sum_=0
    for i in range(len(string)):
        sum_=sum_+int(string[i])
    return sum_

def factorial(x):
    fact=x
    while x!=1:
        fact=fact*(x-1)
        x=x-1
    return fact

# From P_16
def sum_of_digits(x):
    string=str(x)
    digits=[]
    for i in range(len(string)):
        digits.append(string[i])
    return sum_of_string(digits)

def sum_of_fact(x):
    return sum_of_digits(factorial(x))


# print(factorial(10))
print(sum_of_fact(100))
