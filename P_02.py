# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
def even_fibonacci(x): #returns the sun of all even numbers of the Fibonacci sequence under the x value
    fib_seq=[1,2]
    while fib_seq[-1] < x:
        fib_seq.append(fib_seq[-2]+fib_seq[-1])
    # return fib_seq

    addi=0

    for i in range(len(fib_seq)):
        if fib_seq[i]%2==0:
            addi=addi+fib_seq[i]
    return addi

print (even_fibonacci(4000000))
