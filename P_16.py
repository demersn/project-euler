# What is the sum of the digits of the number 21000?

#print(2**1000)

def sum_of_string(string):
    sum_=0
    for i in range(len(string)):
        sum_=sum_+int(string[i])
    return sum_

def sum_of_digits(x):
    string=str(x)
    digits=[]
    for i in range(len(string)):
        digits.append(string[i])
    return sum_of_string(digits)

print(sum_of_digits(2**1000))
